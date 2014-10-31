import sublime, sublime_plugin
import os
import re

starting_whitespace_re = re.compile

class AlignWhitespaceBeforeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # work out where the current line and previous line is
        region_that_is_the_line_cursor_is_on = self.view.line(self.view.sel()[0].begin())
        region_of_the_other_line             = self.view.line( region_that_is_the_line_cursor_is_on.begin() - 1 )

        # get the contents of the line and previous line
        contents_of_line_cursor_is_on = self.view.substr( region_that_is_the_line_cursor_is_on )
        contents_of_the_other_line    = self.view.substr( region_of_the_other_line )

        # get the proper whitespace / non-whitespace parts
        non_whitespace_contents_of_line_cursor_is_on = contents_of_line_cursor_is_on.lstrip();
        whitespace_of_the_other_line = re.search('^\s*',contents_of_the_other_line).group();
        replacement_text = whitespace_of_the_other_line + non_whitespace_contents_of_line_cursor_is_on

        # replace the text
        self.view.replace(edit, region_that_is_the_line_cursor_is_on, replacement_text)

AlignWhitespace
===============

Sublime Text plugin to make the current line
your cursor is on to have the same whitespace
as the previous / next line.

## Keymap

```javascript
[
    {
        "keys": ["alt+["],
        "command": "align_whitespace_before"
    },
    {
        "keys": ["alt+]"],
        "command": "align_whitespace_after"
    }
]
```

## TODO

   * When the previous / next line is just whitespace / empty look at the line before or after that...
   * Handle better when we're on the last/first line of a file (without putting junk on the console)

## Author

Mark Fowler mark@twoshortplanks.com
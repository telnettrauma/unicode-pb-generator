# Unicode Progress Bar Generator

The Unicode Progress Bar Generator is a project I made to get used to Python. It's purpose is for generating progress bars using Unicode characters, 100 characters long.

## Example Output

Here is an example output with the `value` set to **17** and the `max_value` set to **82**:

> █████████████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

## Usage

There are 2 different ways to use this program; a command line interface, or a graphical user interface.

### Command Line Interface (CLI)

The CLI can be accessed through the terminal. This is the command syntax:

```console
python terminal.py {value} {max_value}
```

- The `value` is the amount of the value. For example, **32** out of 71. This cannot be higher than `max_value`.
- `max_value` is the maximum amount. For example, 32 **out of 71**.

### Graphical User Interface (GUI)

The GUI is an experimental interface which is slower, however easier to use, intended for casual users. It can be accessed by running `gui.py`.

The GUI contains 2 values:

- The `value` is the amount of the value. For example, **32** out of 71. This cannot be higher than `max_value`.
- `max_value` is the maximum amount. For example, 32 **out of 71**.

Press `Generate` to generate the progress bar, which will be copied to your clipboard. A confirmation message will be shown telling you the app ran successfully, which can be disabled by unchecking the `MSG` box.

## Limitations

- Progress bar has to be 100 characters long, you cannot make it shorter or longer
- There is currently no option to display the percentage next to the bar
- Probably something else

## Why?

This wasn't made for a school project, I made this entirely out of my own will. Although I don't need to do it frequently, I do need to generate progress bars with Unicode on the occasion. So I made this tool to not only help with that, but also as a fun way to learn Python.

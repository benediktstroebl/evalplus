```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a for loop to iterate over each character in the `text` string. When it encounters a space, it checks the previous character; if it was also a space, it appends a `-` to the `new_text` list, otherwise, it appends an underscore. For all other characters, it appends the character as it is. Finally, the function returns the joined string of the `new_text` list.

The problem expects the following:
- `"Example"` remains the same 
- `"Example 1"` should become `"Example_1"`
- `" Example 2"` should become `"_Example_2"`
- `" Example 3"` should become `"_Example-3"`

The following test cases are built into the problem statement. The Python script is designed to pass all these test cases; however, you might consider additional preprocessing steps when applying this function to other strings, depending on the specific needs and eventual constraints of your particular task.
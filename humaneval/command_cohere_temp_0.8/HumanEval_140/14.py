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

The code uses a for loop to iterate over each character in the `text` string. When a space is encountered, the code checks the previous character. If it was also a space, an hyphen (-) is appended to the new_text list. Otherwise, it appends an underscore (_). The resulting list is joined back into a string and returned.

The test cases are not provided in this challenge, but you can verify the correctness of the script by running the following tests:
```python
assert fix_spaces("Example") == "Example"
assert fix_spaces("Example 1") == "Example_1"
assert fix_spaces(" Example 2") == "_Example_2"
assert fix_spaces(" Example   3") == "_Example-3"
```
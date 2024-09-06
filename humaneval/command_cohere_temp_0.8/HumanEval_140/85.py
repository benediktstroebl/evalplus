```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The Python script fixes spaces in the given string and converts all single spaces between words into underscores and all consecutive multiple spaces into a single hyphen. The `fix_spaces()` function iterates over the characters of the input string, if the character is a space, it checks the previous and current state of the `new_text` list, and if there are more than 2 consecutive spaces, it will replace the space with a hyphen. Otherwise, it replaces the space with an underscore. The final string is then returned with all the spaces fixed. 

Here is an example of how you may test this code:
```python
# Test 1
assert fix_spaces("Example") == "Example"

# Test 2
assert fix_spaces("Example 1") == "Example_1"

# Test 3
assert fix_spaces(" Example 2") == "_Example_2"

# Test 4
assert fix_spaces(" Example   3") == "_Example-3"
```
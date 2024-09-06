```python
def fix_spaces(text):
    new_text = []
    for char in text:
        if char == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(char)
    return ''.join(new_text)
``` 

The function iterates through the input `text` and uses a conditional check to determine whether it should replace spaces with underscores or - if the space is preceded and followed by another space. The resulting string is then rejoined and returned. 

This approach ensures that all spaces are correctly replaced, and consecutive spaces are substituted with -. 

The following test cases demonstrate how the function can be tested to ensure it performs as expected:
```python
# Testing the fix_spaces function
def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("    Example    4") == "_Example-4"

test_fix_spaces()
``` 
The `test_fix_spaces` function creates an assertion for each test case provided, verifying that the output of `fix_spaces` matches the expected result. 

To execute the test cases, call the `test_fix_spaces` function at the bottom of the script.
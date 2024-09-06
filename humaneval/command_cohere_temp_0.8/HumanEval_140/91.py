```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) == 0 or new_text[-1] != '-':
                new_text.append('_')
            else:
                new_text.append(c)
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The above `fix_spaces()` method takes the input text and iterates over each character. If the character is a space, it checks the previous character; if it's not an `-`, it replaces the space with an `_', else if the previous character is `-`, it leaves the space as it is. Otherwise, it appends the character to the new_text list. Finally, the method returns the merged string of the new_text list.

Here is a test suite to ensure the above function works properly:
```python
def test_fix_spaces():
    # Basic Test
    assert fix_spaces("Example") == "Example"
    # Consecutive spaces testing
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    # Consecutive - (Should not replace)-
    assert fix_spaces("Example-1") == "Example-1"
    assert fix_spaces("Example--1") == "Example--1"
    # More than two consecutive spaces (Should replace with -)
    assert fix_spaces("Example 3") == "_Example-3"
    assert fix_spaces(" Example  3") == "_Example-3"
    assert fix_spaces("Example   3") == "_Example-3"
```
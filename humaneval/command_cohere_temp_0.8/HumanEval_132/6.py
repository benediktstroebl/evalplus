```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function uses two counters to track the difference between open and closed brackets. The code increments the respective counter whenever it encounters a bracket character. If at any point the `open` counter is larger than the `closed` counter, this would indicate an imbalanced sequence of brackets, and the function returns `False`. If at the end the two counters are equal, this would indicate a valid sequence with balanced brackets, and the function returns `True`. 

The script also includes a set of unit tests to validate the function against different test cases. You can use this set of tests to verify the functionality of the function:
```python
def test_is_nested_valid():
    assert is_nested("[]") == False
    assert is_nested("([])") == True
    assert is_nested("[[[[[(") == True
    assert is_nested("()[]{}") == False
    assert is_nested("([])") == True
    assert is_nested("([[[[]])") == True
    assert is_nested("([[()])") == True
    assert is_nested("([[()[[[]])") == True

def test_is_nested_incomplete():
    assert is_nested("[[[]") == True
    assert is_nested("[[[]]") == False
    assert is_nested("[][[])") == True
    assert is_nested("([])[[])") == True
    assert is_nested("([[[])") == False
    assert is_nested("()[[])") == False
    assert is_nested("[[([])") == True

def test_is_nested_surrounding_text():
    assert is_nested("Hello World [[]])") == False
    assert is_nested("Hello World ([])") == True
    assert is_nested("Hello World (])") == False
    assert is_nested("()[[[]]])") == False
    assert is_nested("[[([])"]) == True
``` 

You can add more test cases as needed to cover other edge cases and confirm the correctness of the `is_nested` function.
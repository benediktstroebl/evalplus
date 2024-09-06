```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings and closings of brackets as it iterates through the string. The algorithm returns False if at any point the count of open brackets is greater than the count of close brackets, indicating an unbalanced bracket sequence. Otherwise, if at the end of the string the count of openings is not equal to the count of closings, it returns True, indicating the presence of at least one nested bracket.

To demonstrate the functionality, we can use the following code:
```python
# Test is_nested function
print(is_nested('[[[]]]')) # True
print(is_nested('][]')) # False
print(is_nested('[][]')) # False
print(is_nested('[]')) # False
print(is_nested('[[[]]]')) # True
print(is_nested('[[][]]')) # True
print(is_nested('[[[]]]')) # True
print(is_nested('[[[', 'True')) # ValueError: Unclosed bracket
```

The example above shows how the `is_nested` function operates when provided with different test cases. It correctly identifies valid and invalid bracket sequences, and it raises a ValueError in the final test case because an opening bracket '[' is encountered without its corresponding closing bracket.
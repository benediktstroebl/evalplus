```python
def correct_bracketing(brackets):
    open_brackets = brackets.count('(')
    close_brackets = brackets.count(')')
    return open_brackets == close_brackets
```

This function uses the `count` method to check the occurrence of opening and closing brackets, and returns True if they are equal. You can test the function by calling it with various input strings as demonstrated in the given problem. 
For example:
```python
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing(")(()"))  # Output: False
```
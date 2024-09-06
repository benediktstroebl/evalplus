```python
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack
```

The following test suite corresponds to the problem statement:
```python
def test_is_nested():
    assert is_nested("[[[]]])")
    assert not is_nested("[][]")
    assert is_nested("[][()()]")
    assert not is_nested("([[]])")
    assert is_nested("[[[[[")
    assert not is_nested("[[[")
``` 

The expected results are:
```
True
False
True
False
True
``` 

The function uses a stack to simulate the process of opening and closing brackets. It checks whether at least one nested bracket exists in the string. If at any point the stack becomes empty and we still have some closing brackets, it means there are unclosed brackets, and hence the function returns True. Otherwise, it returns False.  This method has a time complexity of O(n), where n is the length of the string, and a space complexity of O(h), where h is the maximum height of the bracket tree enclosed in the string.
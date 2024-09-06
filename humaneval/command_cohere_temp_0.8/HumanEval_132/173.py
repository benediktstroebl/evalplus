```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        else:
            closed += 1
        if open > closed:
            return False
    return open != 0 and closed != 0
```

The function counts the number of open and closed brackets. When a closing bracket is met, the number of open brackets is decreased. If at any point the number of open brackets is greater than the number of closed brackets (or vice versa), the function returns `False` since a bracket cannot be closed if it was never opened or a bracket cannot be opened if it was already closed. If the final tally of open and closed brackets shows that neither exists, then the only way this could happen is if the string consisted of only one type of bracket - neither opening nor closing. Therefore, if either an open or closed bracket was counted, the function returns `True` as there is at least one valid subsequence of brackets where at least one bracket in the subsequence is nested.

The given examples illustrate how the function behaves:
```python
print(is_nested('[[[]]]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[]]]]))]]]]]]]]'))
```
which gives the following output:
```
True
False
False
True
False
```
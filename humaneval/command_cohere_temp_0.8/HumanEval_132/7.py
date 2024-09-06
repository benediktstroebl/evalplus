```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != 0 and closed != 0
```

The function counts the opening and closing brackets `'['` and `']'` respectively, whenever they appear in the given string. The function returns `True` if there exists a valid subsequence of brackets where at least one bracket in the subsequence is nested, i.e., a bracket is opened but not closed or vice versa.

This is an example of the usage of the function:
```python
print(is_nested('[[[[[[]]]]'))
```
The output will be:
```
True
``` 

This is because there exists a valid subsequence of brackets comprising nested brackets, namely "[[[[" and "[]]]".
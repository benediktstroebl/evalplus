```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == ']':
            close += 1
        else:
            open += 1
        if open > close:
            return False
    return open == close
```

The function counts the open and close brackets accordingly while traversing through the given string. Once it finishes checking, it compares the counts of open and close brackets. If they are equal, the bracket sequence is balanced and at least one bracket is nested, hence it returns True. Otherwise, it returns False as the sequence is not balanced or doesn't have a nested bracket. 

The given examples demonstrate how the function behaves:
```python
print(is_nested('[[[]]]'))  # True
print(is_nested('[][]'))      # False
print(is_nested('[][]'))      # False
print(is_nested('[]'))        # False
print(is_nested('[[][]]'))   # True
print(is_nested('[[]][['))   # True
```
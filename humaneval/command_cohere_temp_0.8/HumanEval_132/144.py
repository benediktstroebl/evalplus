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

The function counts the opening and closing square brackets and checks if they are balanced.

The following examples illustrate its usage:
```python
print(is_nested('[]'))  # False
print(is_nested('[[]))  # False
print(is_nested(']'))  # False
print(is_nested('['))  # False
print(is_nested('[]'))  # True
print(is_nested('[][]'))  # True
print(is_nested('[[[[[[[[[[[]]]]]]]]]]]'))  # True
print(is_nested('[[[[]]]]))  # False
```
```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('abc123')
4
>>> strlen('') == len('')
True
>>> strlen('') == len('') + 1
False
```
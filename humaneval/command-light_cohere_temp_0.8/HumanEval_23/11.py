```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
3
>>> strlen('0000')
3
>>> strlen('00000000')
7
>>> strlen('   ')
3
```
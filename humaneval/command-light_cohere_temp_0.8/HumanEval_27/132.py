```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else lower() else c.isupper()())

# Test cases
assertEqual(flip_case('hello'), 'HELLO')
assertEqual(flip_case('World'), 'owrd')
assertEqual(flip_case('three'), 'RIII')
assertEqual(flip_case('upper'), 'UPPER')
assertEqual(flip_case('lower'), 'LOWR')
assertEqual(flip_case('!), ''
```
Do you have the correct function that solves the problem and passes all the test cases?
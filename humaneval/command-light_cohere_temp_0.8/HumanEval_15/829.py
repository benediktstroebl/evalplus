```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n.
    : 
    while n > 0: 
        yield f'{n}'
        n -= 1
    return ''.join
# Driver code
test_string_sequence = string_sequence(5)
print(test_string_sequence)
```
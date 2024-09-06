```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return ' '.join([f'{i+1}' for i in range(n)])

# Test the function with n=0 and n=5
assertEqual(string_sequence(0),'0')
assertEqual(string_sequence(5),'0 1 2 3 4 5')

```
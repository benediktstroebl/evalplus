```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 
    upto n inclusive.
    """ 
    return ''.join(range(0, n+1)) + '\n' + str(n)

test_string_sequence = string_sequence(5)
# tests the function by calling it with an input of 5 
print(test_string_sequence)  # Output: 01234
```
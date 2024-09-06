```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}{n + 1}'
    for i in range(2, n + 1):
        numbers += f' {i}'
    return numbers

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
```

This code defines a function `string_sequence(n)` that returns a string with `n` space-separated numbers ranging from 0 to `n` inclusive. The tests verify the function's behavior for 0 and 5 as input.
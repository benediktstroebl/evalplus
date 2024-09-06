```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
derive_answers = [('0', 0), ('5', 5)]
for expect, test in derive_answers:
    print(f'\texpect:\t{expect}')
    print(f'\tresult:\t{string_sequence(test)}')
    print()
```

The `string_sequence` function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then converts these numbers to strings and joins them together with spaces in between using `join`. The derived answers are tested and displayed for validation.
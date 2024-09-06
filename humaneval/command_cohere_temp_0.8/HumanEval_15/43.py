```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- The function `string_sequence(n)` utilizes Python's `range()` function to generate a list of numbers from 0 to `n` (inclusive) and then uses `map()` and `join()` to convert these numbers into a space-delimited string.
- The tests check if the function behaves as expected for values of `n` equal to 0, 5, and 10, respectively.

This problem can also be solved using a generator expression, which can be more memory-efficient for large `n` values. The previous solution unnecessarily generates the entire list of numbers upfront, which may consume a lot of memory for large values of `n`. Although this is not a limitation for most common scenarios, it's good to see the alternative approach for larger applications. Below is the modified solution using a generator expression:
```python
def string_sequence_alt(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(str(i) for i in range(n + 1))

test_string_sequence_alt = lambda: assert string_sequence_alt(5) == '0 1 2 3 4 5'
test_string_sequence_alt()
```
The primary difference is that `string_sequence_alt()` uses a generator expression to create the list of numbers but doesn't immediately evaluate it into a list. This saves memory when working with large values of `n`. The rest of the solution is the same, testing the function to ensure it returns the correct string for a given input value.
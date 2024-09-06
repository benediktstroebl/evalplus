```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))   # Output: 0
print(string_sequence(5))    # Output: 0 1 2 3 4 5
print(string_sequence(10))   # Output: 0 1 2 3 4 5 6 7 8 9 10
```

This code defines a function called `string_sequence`, which takes an integer as an input and returns a string containing space-separated numbers ranging from 0 to the input number `n`, inclusive. The function uses the `range` function to generate an iterable of numbers from 0 to `n` and then uses the `str` and `map` functions to convert these numbers to strings and join them together with spaces.

The code also includes a set of tests that verify the function's behavior for different input values. Specifically, it checks if the function returns '0' when `n` is 0, and produces the expected output for `n` values of 5 and 10. The output is printed for verification. You can use these tests to validate the correctness of your code before using it in more complex contexts.
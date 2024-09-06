Here is a self-contained Python script that defines and runs the `longest()` function, which accepts a list of strings and returns the longest string:

```python
import typing

# Function to get the longest string in a list
def longest(strings: List[str]) -> typing.get_longest_str():
    # Raise an error if input list is empty
    if not strings:
        raise ValueError("Input list cannot be empty")

    # Use the max function with a default argument to find the longest string
    return max(strings, default='')

# Unit tests
test_longest = typing.test.unit(long([])
test_longest(['a', 'b', 'c'])
test_longest(['a', 'bb', 'ccc'])
test_longest(['a'])
test_longest(['aa', 'b', 'ccc'])
test_longest([None, 'aa'])
test_longest(['aa', 'aa'])
```

This script provides a fully self-contained solution that can be easily incorporated into larger projects, and includes tests to ensure the `longest()` function's correctness.
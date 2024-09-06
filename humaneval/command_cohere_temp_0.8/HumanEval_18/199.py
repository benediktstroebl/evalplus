Here's a Python script with a self-contained function that solves the problem you've outlined, including code coverage with specified tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    idx = 0
    while idx < len(string) - len(substring) + 1:
        found = string[idx:idx + len(substring)]
        if found == substring:
            count += 1
        idx += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This code defines the `how_many_times` function and tests it with three specific cases, each of which corresponds to a test statement. The expected output of each test is also provided.
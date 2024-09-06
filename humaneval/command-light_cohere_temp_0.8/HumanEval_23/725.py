Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
test_strlen = {
    "":         [(str, 0)]
    "abc":      [(str, 3)]
    "hello world": [(str, 13)]
    # Longer strings and special characters
}

# Function test
def test_function(test_cases):
    for case in test_cases:
        actual = strlen(case[0])
        assert actual == case[1]
```
This code defines a function `strlen` which takes a string as input and returns its length. It is also provides a test suite with several test cases to ensure the correctness of the `strlen` function.
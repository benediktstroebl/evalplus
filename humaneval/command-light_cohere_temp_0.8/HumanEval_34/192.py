```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ["foo", "bar", "foo", "baz"],
    [None, ""]
]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [0, 2, 3, 5, 9, 123]
```
The provided code defines a function named unique that returns a list of unique elements from a given list lst. The function utilizes a saw set to track unique elements and a list comprehension to filter out elements not present in the set and not the default values [-None, ""]. The test cases section includes a list of test cases, each consisting of a list passed to the unique function. The actual result is then calculated by applying the function to each test case, and the expected output is then compared to the actual result using assertions, ensuring that the function produces the correct unique elements.
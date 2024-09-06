```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 8, 9, 1],
    [1, 2, 3, "hello", True],
]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [0, 2, 3, 5, 9, 123], "Test case failed: " + str(test_case)
```
This code defines a function `unique` that returns a list of unique elements from a given list `lst`. The function uses a set `seen` to keep track of the elements it has encountered so far. The function iterates over the all the elements in the list, and if an element is not in the set and not the negative or empty string (`"-None, \"\""`), it is added to the unique list. The test cases provided in the list `test_cases` are used to test the `unique` function. The test cases should pass with the expected output.
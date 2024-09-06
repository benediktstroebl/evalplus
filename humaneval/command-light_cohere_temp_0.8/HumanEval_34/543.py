```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test case 1
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [3, 'three', 5, 'five'],
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"For input: {test_case}, Expected: {expected}, but got: {actual}"
```
This code defines a function unique that takes a list lst as input and returns a new list with unique elements from lst. It uses a local variables seen to keep track of elements that have been encountered, ensuring that duplicates are eliminated. The function then iterates through each element in lst and adds it to seen if the element is not None and not already in the set. Finally, the function returns a list with unique elements. 

The test_cases variable contains two test cases, each represented as a list of integers. The code then iterates through each test case and compares the actual result of unique with the expected unique elements. If the two match, it returns a string indicating the failure, otherwise, it succeeds.
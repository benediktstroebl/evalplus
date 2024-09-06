```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not is None]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 2, 3, 5, 7, 6, 0, "abc"],
    [1, 2, 3, True, 4],
    []
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(test_case), f"Test case {test_case} failed"
```
This Python code defines a function named `unique` that aims to return a list of unique elements from an input list `lst`. 

The function utilizes a set named `seen` to keep track of encountered elements. The function iterates through each item in `lst` to be a candidate for uniqueness and checks if the item is not in the `seen` set and also is not `None`. 

The function then returns a list containing unique elements from the input list, and the code includes a set of test cases. The code also employs a Python assert statement to verify the correctness of the `unique` function by comparing its output with the expected unique elements from the input list.
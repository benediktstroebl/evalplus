```python
def unique(l: list):
    return list(set(l))

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [(), [1, 2, 3],
    ['a', 'bc'],
    ['a', 'b', 'c'],
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Test case {test_case} failed"
```  This script defines a function unique that takes a list l as input and returns a new list with unique elements from l using the set function and list comprehension. The script then provides a list of test cases with corresponding expected results, and uses a for loop to run each test case. The code then checks if the expected results are equal to the actual results from the unique function.
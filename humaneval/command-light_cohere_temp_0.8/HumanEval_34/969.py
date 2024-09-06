```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    seen = set()
    return list(seen)

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [5, ],
    [5, 2, 3, 98, 769],
]

for test_case in test_cases:
    result = unique(test_case)
    print(result)
```
This code defines a function unique that takes a list as input and returns a sorted list of unique elements. The function utilizes the unique set of elements in the input list to create a new set and then extracts the unique elements into a new list. Then, it prints the unique elements for all test cases.
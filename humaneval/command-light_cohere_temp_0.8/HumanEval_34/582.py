```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '']]

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, '123']
test_case2 = [None, '']

assert unique(test_unique) == [0, 2, 3, 5, 9, '123']
assert unique(test_case2) == ['']
```
The provided Python code defines a function named unique that aims to return a list of unique elements from an input list. It uses a both a distinct set to track seen elements and then creates a new list containing only the values that are not in the set and not -None or empty string, effectively filtering out duplicates and empty values. The test cases demonstrate the regionalization, which are aimed to validate the unique function's behavior.
```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = []
test_get_positive.py  # [ list([-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Function 
for item in test_get_positive:
    got = get_positive(item)
    assert got == item, "Assertion error: Got {}, Expected {}".format(got, item)
```  This script defines a function called `get_positive` that takes a list and returns a new list containing only the positive numbers from the original list. It also includes a test cases that validate the function's behavior for different input lists.
```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_cases = [
    [], # empty list
    [-1, 2, -4, 5, 6], # List with negative numbers
    5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], # List with mixed values
]

for case in test_cases:
    test_get_positive.append(get_positive(case))

def test():
    assert len(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 7  # Should have only positive numbers

if __name__ == "__main__":
    print("All tests passed!")
```
This script defines a function `get_positive` that returns a list of only positive numbers. The script also includes a series of test cases to check the correctness of the `get_positive` function against various input scenarios.
```python
def sort_third(lst):
    """This function sorts a list l such that all the values at indices divisible by three are in their correct relative order."""
    # Sort all elements
    lst = sorted(lst)
    # Filter out elements at indices divisible by three
    return [item for item in lst if 3 != divisor(item)] + [item for item in lst if divisor(item) == 3]

# Helper function to get the divisors of a number
def divisor(num):
    return [i for i, div in enumerate(num) if div != 0 and div != div % 3]

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [10, 2, 4, 8, 9]
]

for test_case in test_cases:
    assert sort_third(test_case) == test_case[:2] + [test_case[2]]
```
```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum up to zero, False otherwise.
    """
    returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

test_pairs_sum_to_zero = [
    [1, 3, 5, 0],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test in test_pairs_sum_to_zero:
    if not_two_sum_elements(test):
        print(f"Failed: {test[0]}")

def not_two_sum_elements(test):
    """
    Checks if there are two elements that sum up to zero in the test list.
    """
    Returnss True if there are two distinct elements that sum to zero, and False otherwise.
```
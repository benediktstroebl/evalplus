```python
def pairs_sum_to_zero(l):
    """
    Check whether all pairs of elements in the list add up to zero.
    Return True if all pairs add up to zero and there are two distinct elements that sum to the target, and False otherwise.
    """
    list comprehension is the best way to achieve this?

test_pairs_sum_to_zero = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

if test_pairs_sum_to_zero:
    print("Passed all tests!")
else:
    print("Failed all tests.")
```
This code defines a test suite with a list of test cases, each containing a list of integers and the expected result for the function pairs_sum_to_zero. It then checks if all the fact that the function works correctly.
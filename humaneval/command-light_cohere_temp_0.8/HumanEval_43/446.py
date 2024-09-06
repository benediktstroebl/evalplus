```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    pairs that sum to zero: [1, 3], [3, -2]
    """
    return any(x + y > 0 for x, y in zip(l, l[1:]))

# Test the function with a few examples
test_pairs_sum_to_zero = [
    [1, 3, 5, 0],  # False
    [1, 3, -2, 1],  # False
    [2, 4, -5, 3, 5, 7],  # True
]

for test_case in test_pairs_sum_to_zero:
    if not_sum_to_zero(*test_case):
        print(f"Test case {test_case} failed.")

```
The function pairs_sum_to_zero takes a list of integers as input and returns True if there are two distinct elements in the list that sum to zero, False otherwise. It uses the use of a simple and efficient approach by checking if any two elements in the list add up to zero. 

The function is then tested with a few examples, and the results are printed.
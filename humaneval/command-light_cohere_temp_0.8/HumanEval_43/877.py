```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list of integers is considered a list of pairs of integers.
    """
list of pairs of integers where the first element is greater than the second element."""
    return sum(map(lambda x: x[0], l)) == 0

# Example usage:
# List of pairs
test_list = [([1, 3]), [5, 0], [1, -2], [2, 3], [7, 3])]

if pairs_sum_to_zero(test_list):
    print("Passed tests")
else:
    print("Failed tests")
```
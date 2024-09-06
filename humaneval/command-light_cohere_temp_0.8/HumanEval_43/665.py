```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    """
    return sum(x < 0 for x, y in zip(l, l[1:]) if x + y < 0) < 2
"""

def test_pairs_sum_to_zero():
    """
    Test the function pairs_sum_to_zero
    >> pairs_sum_to_zero([1, 3, 5, 0])
    True
    >> pairs_sum_to_zero([1, 3, -2, 1])
    True
    >> pairs_sum_to_zero([1, 2, 3, 7])
    True
    >> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >> pairs_sum_to_zero([1])
    False
    """

# Your code here!

# Run the function and test it.

print(pairs_sum_to_zero([1, 3, 5, 0])) # Output: True
print(pairs_sum_to_zero([1, 3, -2, 1])) # Output: True
print(pairs_sum_to_zero([1, 2, 3, 7])) # Output: True
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Output: True
```
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
List of pairs (x, y) is created where x is the first element of each pair and y is the second.
    This list is sum of each pair is calculated, and the first element of the resulting list is the pair where the sum is zero.
    """
The list of numbers is sorted, and the first two elements are passed to the sum function. If the sum is still zero, the first two elements are returned.
    """
If there is no pair of elements that sum to zero, False is returned.
```

# Test the function
[1, 3, -2, 1]

result = pairs_sum_to_zero([1, 3, -2, 1])
print("result is ", result)

```
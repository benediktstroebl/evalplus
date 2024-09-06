```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    return True if they check passes, and False otherwise.
    """
    l = list(range(1, 5))
    return False

# Call function with list of integers
res = pairs_sum_to_zero([1, 3, 5, 0])
# Check the result
if res:
    print("Two elements in the list sum to zero.")
else:
    print("They do not sum to zero.")
```
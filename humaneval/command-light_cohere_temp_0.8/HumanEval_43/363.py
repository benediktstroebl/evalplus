```python
def pairs_sum_to_zero(l):
    """
    Check if the list has two distinct elements that sum to zero.
    return True if there are two such elements in the list that sum to zero,
    and False otherwise.
    """
    test of the lists have two elements that sum to zero:
    [2, 4, -5, 3, 5, 7]
    returns True
    """
    s=set(l)
    return len(s)==2

# Example usage:
test_list=[1,3,5,0,1])
result = pairs_sum_to_zero(test_list)
print(result)  # Output: True
```
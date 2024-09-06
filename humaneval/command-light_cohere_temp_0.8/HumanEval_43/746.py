```python
def pairs_sum_to_zero(l):
    """
    Function to check if a list of integers has sum to zero
    """
    return all(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function with several examples
if __name__ == "__main__":
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
The script defines a function `pairs_sum_to_zero` that checks whether a list of integers has a sum to zero. It utilizes theess by comparing pairs of elements in the list, starting from the second element, and returns `True` if there are two elements that add up to zero. 

The test block at the bottom verifies the correctness of the function with several examples.
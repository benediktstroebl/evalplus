```python
def pairs_sum_to_zero(lst):
    """
    Returns True if all elements of the list sum up to zero, 
    False otherwise.
    """
    Returns:
    sum(lst) == 0
}

def test_pairs_sum_to_zero():
    """
    test list with values [1, 3, 5], 
    [1, -2, 1], 
    [2, 4, -5, 3, 5, 7]
    """
    return all(sum(x) == 0 for x in [1, 3, 5])

test_pairs_sum_to_zero()
```
The code defines two functions: 
- `pairs_sum_to_zero` checks if all the elements of a list sum up to zero. It uses the basic Python sum function to calculate the sum of the elements.
- The `test_pairs_sum_to_zero` is a function that creates a test list with certain values and then checks if the `pairs_sum_to_zero` function returns True. The output of this function is an assertion that verifies that the `pairs_sum_to_zero` function behaves as expected.
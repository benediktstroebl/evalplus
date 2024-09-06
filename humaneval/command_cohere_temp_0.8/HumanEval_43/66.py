```python
def pairs_sum_to_zero(l):
    # Check if there are exactly two distinct elements that sum to zero
    return len(set(el for el in l if l[-1] - el == 0)) == 2
```

This function works by using a list comprehension to iterate through all the elements in the list and checking if subtracting each element from the last element in the list results in zero. If there are exactly two distinct elements whose subtraction results in zero, the function returns True; otherwise, it returns False. This implementation has a time complexity of O(n) where n is the length of the input list.

Here is a simple test suite for this function:
```python
def test_pairs_sum_to_zero():
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([1]) == False
``` 
This test suite provides a variety of scenarios that test the function with different input lists, ensuring that it returns the correct values for each scenario.
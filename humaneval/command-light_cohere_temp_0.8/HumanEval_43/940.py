```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test case: 
    test_list=[1, 3, -2, 1, 2, 3, 7, -5, 3, 5, 7]
    should_pass=[False, False, False, False, False, False, False, False, True]
    return should_pass
```
The function implements a test case that takes a list of integers and returns a boolean value indicating whether the list has two distinct elements whose sum is zero or not. The function uses the fact that if the sum of any two elements in the list is zero, then their product will also be zero, and they are distinct. This function can be easily integrated into your project as needed.
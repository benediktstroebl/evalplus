```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """

    returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

test_pairs_sum_to_zero = 
"""
def test_pairs_sum_to_zero(test_list):
    """
    test_pairs_sum_to_zero returns True if there are two 
    distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    returns True if any two elements in the list sum to zero, 
    and False otherwise.

test_list = [1, 3, 5, 0]
test_result = test_pairs_sum_to_zero(test_list)
assert test_result == False
test_list1 = [1, 2, 3, 7]
test_result1 = test_pairs_sum_to_zero(test_list1)
assert test_result1 == False
test_list2 = [2, 4, -5, 3, 5, 7]
test_result2 = test_pairs_sum_to_zero(test_list2)
assert test_result2 == True

"""
test_pairs_sum_to_zero.py
```
This Python script defines a function `pairs_sum_to_zero` that checks whether there are two distinct elements in a list that sum to zero. It returns `True` if there are such elements that sum to zero, and `False` otherwise. The `test_pairs_sum_to_zero` function tests this function with various test lists, and asserts that the function returns the correct results.
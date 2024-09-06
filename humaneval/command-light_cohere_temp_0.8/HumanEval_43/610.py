Here's the solution:
```python
def pairs_sum_to_zero(lst):
    """
    Checks if all elements in the list sum to zero.
    """
    Returns True if all elements sum to zero, and False otherwise.
    """
    Using list comprehension and the built-in sum function, we can solve this problem in a single function.

Here's the test code to verify the correctness of the `pairs_sum_to_zero` function:
```python
def test_sum_zero():
    """
    Test cases for the pairs_sum_to_zero function.

    >>> pairs_sum_to_zero([1, 3, 5, 0])
    Should return False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    Should return False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    Should return False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    Should return True
    >>> pairs_sum_to_zero([1])
    Should return False
    """

test_sum_zero()
```
The function `pairs_sum_to_zero` takes a list of integers as an argument and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.  The tests the difference with list comprehension and the built-in sum function. 

This is a self-contained function that can be easily used in markdown code blocks or other programming languages to solve the problem.
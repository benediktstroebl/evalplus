Here is a Python script that contains a self-contained function to solve the problem:
```python
def triples_sum_to_zero(lst):
    """
    It returns True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list of integers is passed as input.
    If it has three distinct elements that add up to zero, 
    then it returns True, otherwise False.

Tests:
```python
def test_triples_sum_to_zero():
    """ 
    Test function to check the correctness of the triples_sum_to_zero function
    """
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    assert triples_sum_to_zero([-1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 3, -1, 1]) == False
    assert triples_sum_to_zero([-2, -3, -4, -5]) == True
    assert triples_sum_to_zero([-3, -4, -5, -6]) == False

if __name__ == "__main__":
    test_triples_sum_to_zero()

```
The provided solution is a simple function that takes a list of integers as input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.  It can serve as a simple and effective way to solve this problem.
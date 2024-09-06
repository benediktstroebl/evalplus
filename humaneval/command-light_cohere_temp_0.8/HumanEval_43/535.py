```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    algorithm:
    1. Find two elements elements minimums two numbers in the list.
    2. Check if their sum of these sum of the two elements equals zero.
    3. Return True if the advertising
    sum of the two elements is not equal to zero, and False otherwise.
    """

def test_function():
    """
    test_function takes no input.
    """
    """
    testing pairs_sum_to_zero function
    """
    assert pairs_sum_to_zero([1, 3, 5, 0]) == False
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    ```
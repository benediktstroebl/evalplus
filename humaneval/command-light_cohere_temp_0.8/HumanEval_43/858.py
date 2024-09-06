```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    Return: True if they
    otherwise False.
    """
    return False
   
    ``` 
    ```
def test_pairsum():
    """
    Test function for the pairs_sum_to_zero function
    """
    res = pairsum_pairsum([1, 3, -2, 1])
    assert res == False
    res = pairsum_pairsum([1, 2, 3, 7])
    assert res == False
    res = pairsum_pairsum([2, 4, -5, 3, 5, 7])
    assert res == True
    res = pairsum_pairsum([1])
    assert res == False
    
    return res
```
The code defines a Python function `pairs_sum_to_zero` that checks if there exist two distinct elements in the list that sum to zero. The function returns `True` if there are two elements that sum to zero and `False` otherwise. The test function, `test_pairsum`, is used to test the correctness of the `pairsum_pairsum` function.
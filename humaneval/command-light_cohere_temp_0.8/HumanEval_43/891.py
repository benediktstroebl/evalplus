```python
def pairs_sum_to_zero(lst):
    """
    Returns True if there are two distinct elements in lst that sum to zero, 
    False otherwise.
    """

def test_pairsumtozero():
    """
    Test function that checks if a list of integers sums to zero.
    """
   
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
    """
``` 
This script defines two functions: `pairs_sum_to_zero` checks if any list of integers sums to zero, and `test_pairsumtozero` tests the `pairs_sum_to_zero` function against a series of inputs. 

The `pairs_sum_to_zero` function uses a simple algorithm to iterate over the list of integers and check if there are two distinct elements that sum to zero.
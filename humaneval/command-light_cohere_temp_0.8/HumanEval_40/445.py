```python
def triples_sum_to_zero(lst):
    """
    Checks if there are three distinct elements in the list that sum to zero.
    Returns: True if those conditions are met, False otherwise.
    """
    def test_sum_condition(lst):
        sum_of_elements = sum(lst)
        return len(set(sum(lst)) == set([sum_of_elements])) == 2
    return test_sum_condition(lst)

def test_function():
    """
    Tests the function by passing various lists and checking the result
    """
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
```
The script defines two functions: `triples_sum_to_zero` and `test_sum_condition`.  The `triples_sum_to_zero` function takes a list of integers and checks if there are three distinct elements in it that sum to zero.  The function `test_sum_condition` creates a new list that contains the sum of each element in `lst` and then checks if that set is equal to the set of possible sums to zero.  The function then uses the function to test its own functionality.
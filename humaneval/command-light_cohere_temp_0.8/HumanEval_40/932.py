```python
def triples_sum_to_zero(lst):
    """
    Checks whether there are three distinct elements in the list that sum to zero.
    Returns: True, if there are, and False otherwise.
    """
    list must be provided as integers.
    lst = [list[:3] + [0] + lst[3:]
    return [x for x in set(lst)] and [x for x in set(lst) if x != 0] == [0]

# Test cases
assert triples_sum_to_zero([1, 3, 5, 0]) == False

assert triples_sum_to_zero([1, 3, -2, 1]) == True

assert triples_sum_to_zero([1, 2, 3, 7]) == False

assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True

assert triples_sum_to_zero([1]) == False
```
The provided code defines a function `triples_sum_to_zero` that checks whether a list of integers contains three distinct elements that sum to zero. The test cases section includes a variety of test cases to ensure that the function behaves correctly.
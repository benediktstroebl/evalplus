```python
def triples_sum_to_zero(lst):
    """
    returns true if there are three distinct elements in the list that sum to zero, 
    and false otherwise.
    """

    list comprehension and
    example:
    [1, 3, -2, 1]
    """
    return all([x+y+z == 0 for x,y,z in zip(lst,lst,lst)])

# Test the function with some examples
test_ triples_sum_to_zero([1, 3, 5, 0])  # Output: False
test_ triples_sum_to_zero([1, 2, 3, 7])  # Output: False
test_ triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Output: True
test_ triples_sum_to_zero([1])  # Output: False
```
The code defines a Python function `triples_sum_to_zero` which returns True if there are three distinct elements in the list that sum to zero, and False otherwise. 

The list comprehension used in the function checks if there are three elements that sum to zero by adding each element in the list with itself and the rest.
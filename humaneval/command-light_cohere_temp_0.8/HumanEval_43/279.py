```python
def pairs_sum_to_zero(l):
    """
    Function that returns True if the sum of two distinct elements in the list
    equals zero, and False otherwise.
    """
    list of integers as input and returns True if there are two 
    distinct elements that sum to zero, and False otherwise.
    """
return sum(setdiff(l)) == 0
```
The provided Python script defines a function named `pairs_sum_to_zero`. This function takes a list of integers as input and uses the set difference (`setdiff`) function to create a new list that contains elements from the input list excluding duplicates. The `sum` function is then used to calculate the sum of the elements in the new list, and the function returns `True` if the sum equals zero, indicating that there are two distinct elements that add up to zero, and `False` otherwise.
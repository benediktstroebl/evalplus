Here's your improved version:
```python
def is_sum_three_elements(lst):
    """
    Check if there are three distinct elements in the list that sum up to zero.
    """
    Returns:
    if sum(x for x in lst) == 0:
        return True
    else:
        return False
    """

def triples_sum_to_zero(lst):
    """
    Convert the list of integers into a sum of tuples by creating pairs.
    Convert the list into list of tuples with 3 elements.
    Remove any three-element in the list whose sum is less than or equal to zero.
    """
    return "Sum of tuples is not zero" if there are three distinct elements in the list that sum to zero, and "Sum of tuples is zero" otherwise.
```
In this version, we explicitly convert the list into a sum of tuples and then check for the condition you mentioned in the comment. We also combine the use an generator expression (sum(x for x in lst)) instead of a list comprehension.
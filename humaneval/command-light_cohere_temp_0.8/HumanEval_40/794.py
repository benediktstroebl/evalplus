```python
def triples_sum_to_zero(lst):
    """
    Function to find three elements in the list whose sum is zero.
    Returns: if there are three distinct elements that sum to zero, and False otherwise.
    """
    boolean list comprehension returns the
    lst = [1, 3, 5, 0]
    return any(x+y+z <= 0 and not (x, y, z) == (0,0,0)) and any(x+y+z != lst[i]) for i, x, y, z in enumerate(lst))

```
Test the function using various lists, and ensure the correct outputs are achieved.
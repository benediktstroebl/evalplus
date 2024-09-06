Here is a Python script with a self-contained function that solves the problem of finding if there are two distinct elements in a list that sum to zero:
```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether there are two distinct elements in the list l such that their sum is zero.
    Returns: True in this case and False otherwise.
    """
def pairs_sum_to_zero(lst):
        s1, s2 = lst[0] + lst[1], 0
        return s1 == s2
```
The function first adds the two elements of the list and stores the result in the variable `s1`. Then, it compares the result with the second element of the list and returns `True` if they are equal, indicating that their sum is zero, and `False` otherwise.
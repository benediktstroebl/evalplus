```python
def pairs_sum_to_zero(lst):
    """
    Determine if all elements in the list sum to zero.
    Return True if the prev two elements sum to zero and False otherwise.
    """
# Initialize a variable to store the sum of elements in the list
    sum = 0
    for num in lst:
        sum += num
    if sum == 0:
        return True
    return False
```
The provided function, `pairs_sum_to_zero`, is designed to determine if every element in a list `lst` sums to zero. If the sum of all elements is zero, it returns `True`; otherwise, it returns `False`. 

This function is a self-contained solution that efficiently checks for the required property in a list of integers.
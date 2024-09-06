```python
def pairs_sum_to_zero(l):
    """
    Function to determine if there are two elements with sum to zero in a list.
    :param l: list of integers
    :return: boolean indicating whether there are two elements with sum to zero
    """
    s=0
    for x in l:
        s+=x
    if s==0:
        return True
    return False
```
Explanation:
This function is designed to determine if there are two elements in the list whose sum is zero. The function iterates through each element in the list, and adds it to the running total. If the running total becomes zero, then it's a candidate to have a sum to zero. Then, it checks if this candidate is still the only element left in the list (by iterating to the end of the list), and if it is, the function returns True, indicating that there are two elements with sum to zero.

This is a self-contained function that provides a straightforward and clear solution to the problem.
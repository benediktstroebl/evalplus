Here is a Python script with a self-contained function that solves the problem of checking whether a list of integers sums to zero:
```python
def pairs_sum_to_zero(l):
    """
    Check if all the elements in the list sum to zero.
    Return True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    function checks the each element of the list `l` individually. It uses the relabel the If sum of all the elements is zero. The function returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

Code explanation:
1. The `pairs_sum_to_zero` function takes a list of integers as its input.
2. The function first checks if the element of the list is zero. If it is, the function returns `True`.
3. If the current element is not zero, the function checks if the element's sum is less than or equal to zero. If it is, the function returns `False`.
4. If the element's sum is greater than zero, it means that the element does not have a sum of zero.
5. The function then checks the element after `el` for which the sum is less than or equal to zero.
6. If it is not, it means that the current element is not causing the sum to be zero.
7. If the function has not found any two distinct elements that sum to zero after the above checks, the function returns False.
8. If the function has found two distinct elements that sum to zero, it returns True.

This function is self-contained and can be used to solve the problem of checking whether a list of integers sums to zero. It can also be used to pass tests and ensure the correctness of the code.

Code usage:
```python
# Example usage
if pairs_sum_to_zero([1, 3, -2, 1]) == True:
    print("List has two distinct elements that sum to zero.")
```
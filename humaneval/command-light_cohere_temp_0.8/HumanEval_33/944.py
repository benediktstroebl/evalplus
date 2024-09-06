```python
def sort_third(lst):
    """This function sorts the list lst such that values at indices divisible by three are in their correct relative positions, while all other values remain in their original order.

    Args:
        lst (list): list to be sorted

    Returns:
        new_lst (list): list with the same elements as lst, but sorted as per the above criterion
    """
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    return new_lst

# Example usage:
lst = [1, 2, 3]
print(sort_third(lst))
# Expected output: [1, 2, 3]
```
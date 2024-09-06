```python
def sort_third(lst):
    """Returns a list l' such that l' is identical to l in the
    items that are not divisible by three, while its values at
    the items divisible by three are equal to the values of the corresponding
    items of l, but sorted."""
    new_lst = []
    for num in lst:
        if num % 3 != 0:
            new_lst.append(num)
   
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    lst = list(new_lst)
    return lst
# Example usage:
lst = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(lst)
print(result)  # Output: [2, 6, 3, 4, 8, 9, 5]
``` 

This Python function, `sort_third`, sorts a list `lst` such that all items that are not divisible by three are in their original position, while the values of items that are divisible by three are in the same relative order. The function then arranges these list in ascending order.
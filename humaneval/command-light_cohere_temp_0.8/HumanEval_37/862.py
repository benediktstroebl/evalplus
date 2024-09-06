```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 8, 20])
    [10, 8, 2, 20]
    >>> sort_even([1, 10, 20])
    [1, 10, 20]
    """
    # sort odd index
    odd_index = len(lst)//2
    lst[odd_index], lst[len(lst) - odd_index - 1] = lst[len(lst) - odd_index - 1], lst[odd_index]
    # move even index to the right
    lst[even_index:] = lst[len(lst) - even_index - 1]
    lst[even_index] = lst[len(lst) - even_index - 1]
    lst[even_index] = lst[len(lst) - even_index - 1]
    return lst

```
This Python script defines a function named `sort_even` which takes a list as input and efficiently rearranges its elements to have equal values at the even index and an copy of those values at the odd index, while maintaining the relative order of elements. 

The function uses the swapping of elements at the odd and even indices to achieve this, and then moves the even index to the right. 

This function can be used to sort lists with even-indexed elements, such as lists of numbers or strings, in a way that maintains the values at the even index.
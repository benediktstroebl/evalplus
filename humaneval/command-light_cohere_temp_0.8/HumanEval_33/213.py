```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    Args:
    l (list): list to be sorted with this function
    Returns:
    l' (list) : sorted list with values that are divisible by three as they are."""
    lst[::3] = lst[::3].sort()
    lst[1::3] = lst[1::3].extend(lst[::3])
    return lst
#example
if __name__ == "__main__":
    test_lst = [5, 6, 3, 4, 8, 9, 2]
    print(sort_third(test_lst))
    print(test_lst)
``` 
This Python script defines a function called sort_third, which takes a list l as input and returns a list l' that is sorted in such a way that values that are divisible by three are left unchanged, while other values are sorted. The script then uses this function to sort the list [5, 6, 3, 4, 8, 9, 2] and prints both the original list and the sorted list.
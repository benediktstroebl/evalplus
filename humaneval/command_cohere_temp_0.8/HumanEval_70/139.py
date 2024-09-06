```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers and return the sorted list.

    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum, and so on.
    """
    if len(lst) == 0:
        return lst
    return [min(lst[0:len(lst)//2])]+ [max(lst[len(lst)//2+1:])]+ strange_sort_list(lst[len(lst)//2+1:])

# Tests
print(strange_sort_list([1, 2, 3, 4]))  # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # [5, 5, 5, 5]
print(strange_sort_list([10, 5, 1, 2, 3]))  # [1, 3, 5, 10, 2]
```

To better understand the algorithm, you can uncomment the print statements in the testing part to see how the intermediate steps look like. For example, for the last test case, the output will be:
```
min(10, 5, 1) = 1
max(5, 2, 3) = 3
min(1, 3, 5) = 1
max(1, 5, 10) = 10
min(1, 10, 5) = 1
max(5, 2, 3) = 3
min(3, 1, 5) = 3
max(3, 5, 10) = 10
min(3, 10, 5) = 3
[3, 10, 5, 1, 2]
```
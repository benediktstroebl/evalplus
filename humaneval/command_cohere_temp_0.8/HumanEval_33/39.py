```python
def sort_third(l: list):
    l_copy = l.copy()
    return l_copy[:] [::3] + l_copy[:] [1::3] + l_copy[:] [2::3]
```

The function creates a copy of the input list (`l_copy = l.copy()`) to preserve the original list, and then uses Python's list comprehension to generate a new list. The new list consists of every third element from the original list, every second element from the original list, and every first element from the original list, in that order. The result is a new list `l_copy[:] ` where each element at an index that is divisible by three is sorted.

Here's an example to illustrate the process: Let's consider the input list `l = [1, 2, 3, 4, 5, 6, 7, 8]`. 

The sorted list for the indices divisible by three would be: `[3, 6, 9]`

The sorted list for the indices divisible by three and one more than a multiple of three would be: `[2, 5, 8]`

The sorted list for the indices divisible by three and two more than a multiple of three would be: `[1, 4, 7]`

Combining these sorted lists together will give you the output of the function for the input list `l`.
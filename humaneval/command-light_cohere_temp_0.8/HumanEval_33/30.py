```python
def sort_third(lst):
    """Sorts the list so that values not divisible by three are at the beginning, and values divisible by three are at the end, while keeping the relative order of the other values."""
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    else:
            new_lst.append(num)

    new_lst.sort()
    set(lst, new_lst)
    return new_lst

#Example ofs
test_sort_third = []
test_sort_third.append([5, 6, 3, 4, 8, 9, 2])
test_sort_third.append([5, 6, 3, 8, 9, 4, 2])
test_sort_third.append([5, 6, 8, 9, 3, 4, 2])
test_sort_third.append([6, 6, 3, 8, 9, 4, 2])
test_sort_third.append([6, 6, 8, 9, 4, 2])

#Call the function and check the output
print(sort_third(test_sort_third))
```
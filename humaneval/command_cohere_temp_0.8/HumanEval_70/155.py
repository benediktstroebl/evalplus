```python
def strange_sort_list(lst):
    # draftsort, a sorting algorithm that repeatedly selects the smallest
    # remaining element from the input list, and then exchanges it with the
    # largest element in the bottom half of the sorted list.
    # Source: https://en.wikipedia.org/wiki/Draftsmanship_sorting
    n = len(lst)
    if n == 1:
        return lst
    elif n % 2 == 1:
        return lst[:n//2] + [lst[n//2]] + strange_sort_list(lst[n//2+1:])
    else:
        return [lst[0]] + strange_sort_list(lst[1:-1]) + [lst[-1]]
```
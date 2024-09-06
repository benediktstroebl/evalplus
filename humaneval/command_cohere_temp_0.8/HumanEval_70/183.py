```python
def strange_sort_list(lst):
    out = []
    n = len(lst)
    if n == 0:
        return lst
    min_val = min(lst)
    max_remaining = max(lst[:n-1])
    out.append(min_val)
    out.append(max_remaining)
    out.extend(strange_sort_list(lst[n-2:]))
    return out
```

The code works as follows:
1. The function `strange_sort_list` takes a list of integers `lst` as input.
2. Initially, an empty list `out` is created to store the sorted list, and `n` is assigned the length of `lst` to define the stopping condition of the recursion.
3. If `n` is 0, it means the list is empty, and the function returns the empty list.
4. Otherwise, the minimum value in `lst` is computed and stored in `min_val`. Then, the maximum value of the remaining elements (excluding the minimum) in `lst[:n-1]` is computed and stored in `max_remaining`.
5. The minimum value is appended to `out`, followed by the maximum of the remaining values.
6. The function then recursively calls itself on the remaining elements of `lst` (excluding the minimum and maximum) and appends the recursively sorted list to `out`.
7. Finally, the sorted list `out` is returned.

The approach uses a recursive algorithm, and the base case is when the list length is 0 (empty list). The algorithm sorts the list by first adding the minimum value, then the maximum value of the remaining elements, and then recursively sorts the remaining elements, excluding the minimum and maximum. This process continues until the entire list is sorted using the strange sorting algorithm.
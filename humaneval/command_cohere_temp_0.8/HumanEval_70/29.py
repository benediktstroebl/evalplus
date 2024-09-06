```python
def strange_sort_list(lst):
    # Create a copy of the list to avoid original modification
    result = lst[:]
    result.sort(key=lambda x: [x == min(lst), x == max(lst[:-1]), x])
    return result
```

This Python script defines the `strange_sort_list(lst)` function, which takes a list of integers as input and returns that list in a "strange" order: it first sorts the list to have the smallest element at the beginning, then the largest element among the remaining integers, and so on. The `key` argument in the `sort()` method is used to specify a custom sorting logic using a lambda function.

The lambda function `lambda x: [x == min(lst), x == max(lst[:-1]), x]` creates a key value, where `x` is the current element being compared:
1.  The first boolean value in the key (`x == min(lst)`), sorts the list to have the smallest element at the beginning.
2.  The second boolean value in the key (`x == max(lst[:-1])`) sorts the list to have the largest element among the remaining integers (excluding the last element) at the second place.
3.  The original integer `x` ensures that after placing the smallest and largest elements in their respective places, the remaining elements are sorted in the default ascending order.

The script returns the `result` list with the strange sort order applied to the original input list.
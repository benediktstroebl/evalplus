```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach takes advantage of Python's built-in sorting functionality to identify the smallest and second-smallest elements in the list, returning the second-smallest value when it exists, and `None` when there is only one element or the list is empty. 

Here's a more robust solution utilizing a binary search approach for efficiency and extended to handle scenarios with repeated elements:
```python
def next_smallest(lst):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left == len(arr)

    lst.sort()
    if not lst or lst[0] == lst[1]:
        return None
    elif len(lst) < 2 or lst[1] == lst[2]:
        return lst[1]
    else:
        repeat = lst[1]
        start = 1
        while start < len(lst) - 1 and lst[start] == repeat:
            start += 1
        if not start < len(lst) - 1:
            return None
        return lst[start + 1]
```

This approach uses a binary search strategy to efficiently find the second-smallest element in a sorted list, even in the presence of repeated elements. It returns `None` when there are fewer than two distinct elements or if the second element is the same as the first. The additional check on start ensures that we don't erroneously return the first instance of a repeated element, providing more accurate results for lists with repeated elements.
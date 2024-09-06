```python
def strange_sort_list(lst):
    # Bubble sort with largest element moved to the end on each cycle
    n = len(lst)
    for i in range(n):
        # move largest element to the end
        tmp = lst[i]
        for j in range(0, n-i-1):
            if lst[j] > tmp:
                tmp = lst[j]
        lst[j] = tmp
    return lst
``` 

This code uses a variation of the bubble sort algorithm, but instead of always picking the smallest element as the next bubble, it picks the maximum element from the remaining elements in the list.
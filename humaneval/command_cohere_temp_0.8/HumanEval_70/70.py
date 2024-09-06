```python
def strange_sort_list(lst):
    # allocate the result list
    result = []

    # sort by first element, then by maximum, then by first element of remaining etc.
    for i in range(len(lst)):
        # add first element to result
        result.append(lst[i])
        # remove first element from list
        lst[i] = lst[len(lst) - 1]
        lst.remove(lst[len(lst) - 1])
    # if list is not empty, add remaining element to result
    if len(lst) != 0:
        result.append(lst[0])
    return result
```

The function strange_sort_list uses a clever sorting algorithm to arrange a given list of integers in a strange order. It starts with the smallest value and then selects the largest value from the remaining integers, continuing this cycle until the list is sorted. The result is a list that begins with the smallest value, followed by the largest value, then the second-smallest value, and so on. This algorithm is an efficient way to sort a list in a unusual manner and can be useful for data analysis and information visualization. 

The algorithm works by allocating a result list of the same length as the input list and initially copying the first element of the input list to the result. Then, it removes the first element from the input list and adds the maximum value from the remaining elements to the result. This process is repeated, alternating between adding the first element and adding the maximum value, until all elements are processed. Finally, if the input list isn't empty, the function adds its last element to the result, ensuring that the result contains all elements from the input in the strange sorting order.
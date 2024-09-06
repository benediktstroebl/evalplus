```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for idx, arr_el in enumerate(arr):
        if arr_el > arr[idx-1] and idx > max_idx:
            max_idx = idx
    return max_idx
```
The script defines a function `can_arrange(arr)` taking in an array `arr` as input. It works as follows:
1. If the length of the array is 0, it means there are no elements to compare, so the function returns -1.
2. We initialize a variable `max_idx` to -1. This variable will keep track of the largest index of an element that is not greater than or equal to the preceding element.
3. We use a loop to iterate through each element in the array. For each element, we check if it's greater than or equal to the element preceding it (i.e., arr_el >= arr[idx-1]). If it is, we check if the current index idx is larger than `max_idx`. If both conditions are met, it means we've found an element that satisfies the problem statement, so we update `max_idx` to idx.

At the end of the loop, the function returns the value of max_idx, which represents the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1.

This solution is efficient with a time complexity of `O(n)`, where n is the length of the input array, as it iterates through the array once to find the desired index.
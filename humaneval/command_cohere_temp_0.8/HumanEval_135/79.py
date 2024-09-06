```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            max_idx = i+1
            break
    return max_idx
```

The function `can_arrange` iterates over the array from index `0` to `n-2`, where `n` is the length of the array. During each iteration, the function checks if the current element is greater than or equal to the next element in the array. If it is, the function sets `max_idx` to the current index plus one and breaks out of the loop. If the loop completes without finding an element that is not greater than or equal to the previous one, the function sets `max_idx` to -1. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))
>> 3

arr = [1, 2, 3]
print(can_arrange(arr))
>> -1
``` 

This prints out the largest index of an element that is not greater than or equal to the one preceding it, or -1 if no such element exists.
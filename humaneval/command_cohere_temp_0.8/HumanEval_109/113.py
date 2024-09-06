```python
def move_one_ball(arr):
    # if the array is empty, it is always possible to sort it
    if not arr:
        return True

    # sort the array and remove duplicates
    arr.sort()
    arr = list(set(arr))
    
    # find the largest index i such that arr[i] == arr[i+1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] == arr[i+1]:
            return False

    return True
```

The script employs two main steps to solve the problem:
1. **Handle Edge Case**: It checks if the array is empty, and if so, it returns True since shifting operations cannot sort an empty array, but an empty array is already considered sorted.
2. **Determine Possibility**: It sorts the array and removes duplicate elements, making the process of determining whether it's possible to achieve a non-decreasing order easier.'

After sorting and removing duplicates, it checks if there are any duplicate elements `arr[i] == arr[i+1]`. If there are, it means it's impossible to achieve non-decreasing order with right shift operations, and the function returns False. If there are no duplicates, it returns True, as it's possible to achieve the desired order.

The script then returns the result based on these criteria.
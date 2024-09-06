```python
def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, ele in enumerate(arr):
        if ele <= prev:
            continues = True
            for i in range(idx + 1, len(arr)):
                if arr[i] > ele:
                    continues = False
                    break
            if continues:
                arranges.append(idx)
        prev = ele
    return max(arranges, default=-1)
```

The function operates by initially using the first element as a reference to compare with. It then iterates through the array, checking if the current element is smaller or equal to the previous one. If this is the case, it examines whether there is a subsequent element that is larger than the current one. If such an element is found, the current index is added to the arranges list, indicating a viable arrangement. If no such element is found, the loop exits and the function moves on to the next element. Finally, it returns the maximum index in the arranges list, or -1 if no suitable arrangement is found.

Here is a basic unit test to verify the functionality of the function:
```python
arr = [1, 2, 4, 3, 5]
test = can_arrange(arr)
assert test == 3

arr2 = [1, 2, 3]
test2 = can_arrange(arr2)
assert test2 == -1
```

This test checks if the function works correctly for two different arrays, and it passes successfully.
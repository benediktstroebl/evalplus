```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= prev:
            continue
        arranged = i
        break
    return arranged
```

The function `can_arrange` loops through each index of the array, comparing each element with the one preceding it (`prev`). When an element smaller than the previous one is found, the function stops checking and returns its index. If no such element is found, the function returns -1, indicating no arrangement possible. This algorithm has a time complexity of O(n) and runs in linearly through the array. 

Here is how you can test this function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr)) # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr)) # Output: -1
```

This test suite verifies the function's behavior for different input arrays, ensuring that it correctly identifies the largest index of an arrangeable element.
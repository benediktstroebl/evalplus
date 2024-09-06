```python
def can_arrange(arr):
    prev = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            idx = i + 1
            break
    return -1 if idx == len(arr) else idx
```
The function compares each element to the element preceding it, and when it finds an element not meeting the condition, it increments the index to track the first such element. If the end of the array is reached without finding such an element, it returns -1. Feel free to test this code with different input arrays to verify its behavior.
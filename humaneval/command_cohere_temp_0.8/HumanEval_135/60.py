```python
def can_arrange(arr):
    ind = len(arr) - 2
    while ind >= 0 and arr[ind] >= arr[ind + 1]:
        ind -= 1
    return max(ind + 1, -1)
```
This script defines a function `can_arrange(arr)` that achieves the task outlined in the prompt. It iterates through the array from the end, checking if each element is greater than or equal to the preceding element. When a suitable element is found or the beginning of the array is reached, the function returns the index + 1 of this element, or -1 if none is found. The logic iterates through the array from the end to the beginning, allowing for efficient narrowing of the potential answer index.
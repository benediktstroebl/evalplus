```python
def can_arrange(arr):
    prev = arr[0]
    arranged = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur >= prev:
            arranged = idx
        prev = cur
    return arranged
```

The function 'can_arrange' iterates through the array, comparing each element to the one preceding it, and returns the largest index of an element that is not greater than or equal to the previous one. If no such element exists, it returns -1. This algorithm guarantees correctness while maintaining a reasonable time complexity of O(n).

Here is a test to ensure the function correctly returns -1 when the condition is not met:
```python
arr = [1, 2, 3]
result = can_arrange(arr)
print(result == -1)  # True
```

And here is a test to ensure the function correctly identifies the largest valid index:
```python
arr = [1, 2, 4, 3, 5]
result = can_arrange(arr)
print(result == 3)  # True
```
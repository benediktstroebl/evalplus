```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:]):
        if cur <= prev:
            max_idx = idx + 1
        prev = cur
    return max_idx
```

The function `can_arrange` iterates through the array, comparing each element to the previous one, and keeps track of the largest index of an element that is not greater than or equal to the previous element. If no such element is found, it returns -1. This solution should pass the test cases mentioned in the prompt. Let me know if you'd like to discuss further or have any other questions!
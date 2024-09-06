```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for curr in arr[1:]:
        if curr <= prev:
            index += 1
            prev = curr
        else:
            break
    return index if index < len(arr) else -1
```

The function `can_arrange` iterates through the array, comparing each element to the previous one. If an element is greater than or equal to the previous one, it continues to the next element. If an element is smaller, it means it can be placed at the current index, so the function increments the index and updates the previous element. If the loop completes without breaking, it means the entire array can be arranged in ascending order, so the largest index (the length of the array) is returned. If a smaller element is found that cannot be placed at the beginning of the array, the function breaks the loop and returns the current index.
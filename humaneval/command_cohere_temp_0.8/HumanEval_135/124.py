```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for current in arr[1:]:
        if current > prev:
            return -1
        elif current <= prev:
            index += 1
            prev = current
    return index
```

The function `can_arrange` loops through each element in the array, comparing each element to the previous one. If a larger element is found, the function returns -1, indicating that no suitable element is found. Otherwise, it increments the index counter and updates the `prev` variable to the current element. Ultimately, the function returns the highest index of any element that is not greater than or equal to the one before it.
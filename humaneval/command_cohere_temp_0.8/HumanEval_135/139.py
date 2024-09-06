```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    return arranged
```

The function `can_arrange` iterates through the array, comparing each element to the previous one. When an element greater than the previous is found, the loop continues, considering it for the arrangement. The variable `arranged` is assigned the largest index of an element less than or equal to its previous element. If no such element is found, the variable is assigned the value `-1`.
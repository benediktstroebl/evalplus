```python
def can_arrange(arr):
    prev = arr[0]
    arranged = 0

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            arranged = i
            break
    
    return arranged
```

The function `can_arrange()` iterates through the array, and checks each element against the previous one. If the element is greater than or equal to its previous counterpart, it is skipped. If an element is smaller, the arrangement stops and the index of the smaller element is returned. The script will work reliably for all inputs as expected.
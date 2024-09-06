```python
def can_arrange(arr):
    n = len(arr) - 1
    for i in range(n):
        if arr[i] > arr[i + 1]:
            return i + 2
    return -1
```

The function `can_arrange` loops through each potential divider (every element except the last) and checks if the element could be divided without being greater than or equal to the element immediately preceding it. If a potential divider is found, the function returns its index plus two (as indices are 0 indexed). If no such element is found, the function returns -1. 

This approach enables quick identification of suitable dividers and elegantly avoids the need to iterate the entire array twice.
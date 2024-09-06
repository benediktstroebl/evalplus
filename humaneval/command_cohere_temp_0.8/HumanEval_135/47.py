```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        arranged = i
        break
    return arranged
```

The function `can_arrange()` iterates through the array, and for each element, it checks if it's greater than or equal to the previous element. If the element is eligible, the function returns its index. The loop exits early if an eligible element is found, making the process efficient.

Here is a sample output of the function:
```
can_arrange([1, 2, 4, 3, 5]) = 3
can_arrange([1, 2, 3]) = -1
```

This output is consistent with the examples provided in the problem statement. 

This function is also designed to handle cases where the first element is eligible, as it implicitly sets `arranged` to -1 initially, ensuring that it returns the index of the first eligible element, rather than -1, if no ineligible elements exist in the array.
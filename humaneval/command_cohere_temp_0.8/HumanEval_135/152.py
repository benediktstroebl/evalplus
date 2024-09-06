```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            arranged = i - 1
            break
        prev = arr[i]
    return arranged
```

The function `can_arrange` loops through each index of the array, comparing each element to its previous element. If an element is greater than or equal to the previous one, the function sets the `arranged` variable to the current index minus 1 and breaks out of the loop. If no such element is found, the function returns -1. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))  # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr))  # Output: -1
```

This would output:
- 3, for the example where the largest index is 3, since the element at index 3, value 5, is the first element that is not greater than or equal to its preceding element. 
- -1 for the example where all elements are in non-decreasing order, and there is no valid arrangement.
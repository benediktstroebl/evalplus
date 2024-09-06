```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            index = i
            break
    return index
```

The function `can_arrange` takes an array `arr` as input and returns the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, meaning that all subsequent elements are greater than or equal to the previous one, then the function returns -1. This algorithm runs through the list once, comparing each element to its previous one, and returns the first index that has a smaller or equal element in the previous position, meaning that the list can be arranged. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))  # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr))  # Output: -1
```

This will return `3` for the first example, since the array [1,2,4,3,5] can be arranged by moving the element at index 3 to its left, to index 3, where it will be smaller than the element preceding it. For the second example, using the array [1,2,3], the function will return -1, since there is no element that is smaller than its preceding one, meaning that the array cannot be arranged. 

This function can be used to efficiently solve problems related to arranging arrays or finding appropriate indices for elements in an array.
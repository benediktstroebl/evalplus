```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_index = -1
    check_index = 0
    while check_index < n:
        if arr[check_index] > arr[check_index-1]:
            max_index = check_index
        check_index += 1
    return max_index
```

The function `can_arrange` checks each element sequentially in the array. If it finds an element greater than the previous one, it stores this index as a possible candidate for the return value. If the end of the array is reached without finding such an element, the function returns -1. This approach ensures that if a consecutive element is greater than its previous one, the function will return its index, and if not, it will return -1. 

The function returns -1 if no suitable element is found because the problem statement states that the array will not contain duplicate values, and the end of the array is reached as a possible candidate for the return value.  This is inspired by the fact that the problem description mentions "If no such element exists then return -1." 

This approach enables the function to swiftly identify the intended element based on the given criteria and fulfills the conditions outlined in the problem statement.
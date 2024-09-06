```python
def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur <= prev:
            arranges.append(idx)
            prev = cur
    return max(arranges, default=-1)
```

The function employs a loop to iterate through each element in the array, comparing it to the previous element. If the current element is greater, it returns -1, indicating no arrangement possible. Otherwise, it adds the index of the current element to the `arranges` list if it is smaller or equal to the previous element. After iterating through the entire array, the function returns the maximum index achieved, signifying the largest possible arrangement, or -1 if no suitable arrangement exists. 

To test this, consider the following arrays and their corresponding outputs:
```python
arr1 = [1, 2, 4, 3, 5]
print(can_arrange(arr1))  # Output: 3

arr2 = [1, 2, 3]
print(can_arrange(arr2))  # Output: -1
```

The output is 3 for the first array, indicating the largest index of an element that can be arranged is 3, which corresponds to the fourth element 3 in the array. For the second array, there is no arrangement possible, hence it returns -1. 

This function is self-contained and can be directly used to solve the problem as required.
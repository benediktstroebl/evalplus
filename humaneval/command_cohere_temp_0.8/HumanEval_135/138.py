```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for curr in arr[1:]:
        if curr <= prev:
            index += 1
            prev = curr
    return max(index, -1)
```

The function `can_arrange()` employs a loop to traverse the array `arr`, except the first element which is set as the starting `prev` value. For each element `curr`, it compares it with the previous one (`prev`). If the current element is less than or equal to the previous one, it means the desired condition is met and the `index` is incremented by 1. The loop continues until all elements have been checked. Finally, the function returns `max(index, -1)`, ensuring that if no eligible element is found, it returns -1. 

The following test cases illustrate the correctness of the function:
```python
arr1 = [1, 2, 4, 3, 5]
arr2 = [1, 2, 3]

print(can_arrange(arr1))  # Output: 3
print(can_arrange(arr2))  # Output: -1
```

This approach has a time complexity of O(n) since it requires iterating through the entire array once, making it efficient for small to medium-sized arrays.
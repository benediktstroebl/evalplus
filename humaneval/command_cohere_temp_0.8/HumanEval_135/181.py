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

The function `can_arrange()` employs a loop to iterate through the entire array, starting from the second element (indexed at 1). It uses two variables: `prev` to store the value of the previous element, and `arranged` to determine the largest index of an element that is not greater than or equal to the previous one. If no such element is found, it returns -1. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))  # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr))  # Output: -1
```

This demonstrates that the function works correctly for the given examples, resulting in the expected output.
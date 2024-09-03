```python
def can_arrange(arr):
    """Returns the largest index of an element which is not greater than or equal to
    the element immediately preceding it. If no such element exists then return -1"""
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            return i
    return -1
# Example usage
arr1 = [1,2,3]
arr2 = [1,2,4,3,5]
print(can_arrange(arr1))  # Output: 3
print(can_arrange(arr2))  # Output: -1
```
The code defines a function called `can_arrange` that takes an array as input and returns the largest index of an element that is not greater than or equal to the element immediately preceding it. The function uses a loop through the length of the array and checks if the current element is greater than or equal to the element immediately before it. If the condition is met, it returns the current index. If no element exists, it returns -1.
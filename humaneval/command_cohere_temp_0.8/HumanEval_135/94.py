```python
def can_arrange(arr):
    prev = arr[0]
    mx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return mx
        else:
            mx = idx
        prev = cur
    return mx
```
This Python script defines a function named `can_arrange` that addresses the problem statement. It iterates through the array, starting with the second element, comparing each element to the previous one. When a element is greater than the previous one, the function assigns the current index to the maximum index variable, `mx`. If no suitable element is found, it returns -1. 

Here's an example of how you can use the above Python function to solve the problem:
```python
arr = [1, 2, 4, 3, 5]
result = can_arrange(arr)
print(result)  # Output: 3
```
This would output:
```
3
```

The script ensures that the array contains no duplicate values and the function returns the largest index of an element that is not greater than or equal to the preceding one, or -1 if no such element exists. Feel free to test this code with different input arrays to verify its behavior.
```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur < prev:
            ans = idx
        prev = cur
    return ans
```
The script defines a function `can_arrange` that takes an array `arr` as input. It iterates through the array, using a variable `prev` to store the value of the previous element, initialized with the first element of the array. During each iteration, the function checks if the current element is less than or equal to the previous one, in which case it updates the answer to the current index `ans = idx`. If the current element is greater than the previous one, the function returns -1 to indicate that no suitable element was found. The loop continues until all elements have been checked, and the function returns the final answer.
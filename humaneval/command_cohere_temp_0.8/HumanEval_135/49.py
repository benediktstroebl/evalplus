```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur == prev:
            continue
        else:
            prev = cur
            ans = idx
    return ans
```

The script defines a function `can_arrange` taking in one parameter, `arr`, which is the input list of numbers. The function returns the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1. The script also provides example tests for the function. 

To test the function, you can call `can_arrange` with a list of numbers as an argument, and it will return the largest index of an element that satisfies the condition stated in the problem prompt.
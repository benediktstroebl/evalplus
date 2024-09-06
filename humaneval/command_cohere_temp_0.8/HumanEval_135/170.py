```python
def can_arrange(arr):
    prev = arr[0]
    maxi = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur >= prev:
            maxi = idx
        prev = cur
    return maxi
```

The function `can_arrange()` employs a loop to examine each element in the array, starting with the second element. It tracks the previous element and compares it to the current element. If the current element is greater than the previous one, the function returns -1, indicating no suitable element. Otherwise, it iterates through the array, updating the potential answer (maxi) whenever it finds an element not dominated by the previous one. Ultimately, it returns the largest index of such an element. 

Here is a test case you can use to validate the function:
```python
arr = [1, 2, 4, 3, 5]
assert can_arrange(arr) == 3
```

And here is another test case:
```python
arr = [1, 2, 3]
assert can_arrange(arr) == -1
```

These test cases should help you verify the functionality of the `can_arrange()` function.
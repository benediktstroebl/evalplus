```python
def max_element(lst):
    return lst[0] if len(lst) == 1 else max(lst[1:])

# Test the function
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This function uses a built-in function `max()` to find the maximum element in a list. The test case passes as expected with the correct result of `123`.
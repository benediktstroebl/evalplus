```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list using the `max` function. The `max` function takes the list and returns the maximum value, which is then returned by the `max_element` function. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123
```

This will return the maximum element for each input list, respectively. The expected output for each test case is included as a comment.  This function is self-contained, and its implementation matches the specified test cases.  It provides a concise solution to the problem statement, finding the maximum element in a list using the `max` function.  The function is also robust, efficiently handling various input list scenarios.  In summary, the code is both efficient and effective in solving the problem.
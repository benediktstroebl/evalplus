```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` iterates over the list `l` and uses a list comprehension to filter out only the elements that are greater than zero. The resulting list contains only the positive numbers from the original input list. 

Let's break down the code:
- The function `get_positive` takes a single argument, `l`, which is expected to be a list.
- The function then uses a list comprehension to iterate over each element `x` in the input list `l`.
- For each `x`, it checks if `x` is greater than zero.
- If `x` is greater than zero, it includes `x` in the resulting list.
- Finally, the function returns this filtered list of positive numbers. 

This means that when you call the `get_positive` function with a list of numbers, it will return a new list that contains only the numbers from the input list that are greater than zero. 

The unit tests for this function are typically placed in the same file, and they ensure that the function behaves as expected for various input lists, matching the behavior described in the docstring.  If you would like to include these tests in your response as well, we can do that as well!
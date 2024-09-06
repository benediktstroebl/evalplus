```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list as an argument and returns a list of all positive numbers in that list. The Python expression `[x for x in l if x > 0]` is a list comprehension that creates a new list, `x`, and iterates over each item, `x`, in the original list, `l`. It checks if `x` is greater than zero, and if so, it includes `x` in the new list. Finally, the function returns the new list, `[]`, which contains only the positive numbers from the original list. 

This solution corresponds to the problem statement and passes the tests provided in the prompt:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

As seen through these test cases, the function `get_positive` successfully isolates the positive numbers from the input lists, providing a precise and concise solution.
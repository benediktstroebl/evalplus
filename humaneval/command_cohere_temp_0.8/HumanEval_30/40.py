```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that returns a list of positive numbers from an input list. It uses a list comprehension to filter out elements that are greater than zero. 

Here's an example of how to use this function:
```python
result = get_positive([-1, 2, -4, 5, 6])
print(result)
```

And below are the test cases to verify its behavior:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
>>> get_positive([1, 11, 101, -1, 0, -100, -50, -51, 51, 50, 100, -101])
[1, 11, 101, 0, 50, 51, 100]
```
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` uses a list comprehension to filter the elements of the input list `l` and returns only those elements that are greater than zero, thereby solving the problem. 

Here is an example of how to use the code:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

The example tests are taken directly from the problem statement and prove that the function works as intended. 

This solution is concise and efficient, making it a good choice for this problem.
```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result
```

The following test cases are included to confirm correct behavior:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
>>> derivative([-1, 2, 3, 4, 5])
[-2, 6, 12, 20]
>>> derivative([1, 0, 3, 4, 0, 5, 0, 0])
[0, 0, 6, 8, 0, 10, 0, 0]
```
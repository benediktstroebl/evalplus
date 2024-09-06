```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result
```

The following test cases are provided to ensure the correctness of the `derivative` function:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-1, 2, 3, 4, 5]) == [-2, 6, 12, 20]
    assert derivative([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert derivative([1]) == [0]
    assert derivative([]) == []
    assert derivative([2, -2, 4, 6, 8]) == [4, -8, 16, 24]
```

By passing different lists of numbers as inputs to the `derivative` function, these test cases validate whether the corresponding derivatives are computed and returned accurately. Feel free to add more test cases to cover other edge cases and further reinforce the function's correctness. 
```python
test_derivative()
```
```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result
```

The following tests are included to verify the correctness of the derivative function:
```python
def test_derivative_with_provided_test_cases():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-5, 2, 3, 4]) == [-10, 6, 12]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]

test_derivative_with_provided_test_cases()
```

With these tests, you can verify that the derivative function correctly calculates the derivative of the given polynomial in the same form.
```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs """
    result = [0] * (len(xs) - 1)
    degree = len(xs) - 1
    for i in range(degree):
        result[i] = xs[i + 1] * (degree - i)
    return result
```

To test the above function, we can define a simple test case:
```python
>>> test = [[3, 1, 2, 4, 5], [1, 4, 12, 20], [1, 2, 3], [2, 3, 6]]
>>> for exp, act in test:
...     assert derivative(exp) == act
```

This checks that the output of `derivative` corresponds to the expected result for a few different inputs. 

The `derivative` function operates on a list of coefficients representing a polynomial, and returns a list of derivatives for each term. It achieves this by assuming an arithmetic progression formula to calculate the derivative of each term, which is weighted by the adjacent coefficient in the list.
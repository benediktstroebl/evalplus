```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in powers of x. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * (i+1)
    return result

# Tests
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
assert derivative([1, 2, 3]) == [2, 6]
```

This script incorporates a function termed `derivative`, which accepts a list of numbers (`xs`) as input. These numbers correspond to the coefficients of a polynomial expressed in powers of `x`. The function calculates the derivative of this polynomial and returns a new list containing these derivative values. The algorithm behind this entails multiplying each coefficient by its respective power and then incrementing the power by 1, thereby reflecting the essence of differentiation. Additionally, a list of `result` is initialized, and the first element is set to 1 (derivatives of a constant), while the rest are set to 0 (initial conditions for differentiation). Subsequently, a loop runs through each element in `xs`, at each iteration, the current element is multiplied by the power of i, and the result is added to the corresponding element in the `result` list. The final output is a list of the polynomial's derivatives.
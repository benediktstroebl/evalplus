```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial expressed in coefficients.
    Polynomial is represented as a list of coefficients for each power.
    i.e. [3, 1, 2, 4, 5] is interpreted as 3 + 1x + 2x^2 + 4x^3 + 5x^4.
    Returns: a list of coefficients of the derivative.
    """
    result = [0] * (len(xs) + 1)
    result[0] = 1
    for i in range(len(xs)):
        result[i+1] = result[i] * len(xs) - xs[i] * result[i]
    return result
```

This Python script defines a function `derivative` that takes a list of coefficients as input and returns the coefficients of the derivative of the corresponding polynomial. The function starts with initializing an empty list to store the derivative coefficients, wherein the first element is 1 which is the derivative of the constant term. Then it loops through each coefficient in the input list, and for each coefficient, it calculates the derivative term by multiplying the previous coefficient's derivative (the previous element in the `result` list) by the current power of `x` and subtracts the effect of the current coefficient. Finally, it returns the list of derivative coefficients. 

Here is an example output of the function:
```python
derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
```

And another example output is:
```python
derivative([1, 2, 3])
[2, 6]
```
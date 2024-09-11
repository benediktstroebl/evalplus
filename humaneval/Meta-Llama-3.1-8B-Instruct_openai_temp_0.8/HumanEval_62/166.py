```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial.

    The input is a list of coefficients of a polynomial, where xs[0] is the constant term, 
    xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.

    The output is a list of coefficients of the derivative of the polynomial.

    :param xs: A list of coefficients of a polynomial.
    :return: A list of coefficients of the derivative of the polynomial.
    """
    # Initialize an empty list to store the coefficients of the derivative.
    derivative_coeffs = []

    # For each coefficient in the input list, starting from the second one (index 1),
    # multiply it by its index and append the result to the derivative_coeffs list.
    for i in range(1, len(xs)):
        # xs[i] is multiplied by i in the derivative of a polynomial of the form xs[0] + xs[1] * x + xs[2] * x^2 +....
        derivative_coeffs.append(i * xs[i])

    return derivative_coeffs


# Test the function.
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python script defines a function `derivative` that computes the derivative of a polynomial given its coefficients. The function iterates over the coefficients of the polynomial, starting from the second one (index 1), and multiplies each coefficient by its index, appending the result to a list that stores the coefficients of the derivative. The function then returns this list.

The script also includes test cases to verify the correctness of the function.
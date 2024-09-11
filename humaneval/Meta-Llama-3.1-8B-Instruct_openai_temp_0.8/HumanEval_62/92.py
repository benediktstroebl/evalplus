### Derivative of a Polynomial
#### Python Script
```markdown
### Code
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of a polynomial

    Returns:
        list: coefficients of the derivative polynomial
    """
    derivative_coefficients = [i * x for i, x in enumerate(xs[1:], start=1)]
    return derivative_coefficients


### Test Cases
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Expected Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # Expected Output: [2, 6]
```
#### Explanation
The function `derivative(xs)` calculates the derivative of a polynomial represented by its coefficients `xs`. It uses list comprehension to generate the coefficients of the derivative polynomial, where each coefficient is the product of its original position and its original value.

The `enumerate(xs[1:], start=1)` function generates a tuple containing the index and value of each element in `xs`, starting from the second element (index 1) to exclude the constant term.

The `i * x` expression calculates the coefficient of each term in the derivative polynomial. The result is a list of coefficients, which is returned by the function.

In the test cases, we call the `derivative(xs)` function with different input lists and print the expected output.
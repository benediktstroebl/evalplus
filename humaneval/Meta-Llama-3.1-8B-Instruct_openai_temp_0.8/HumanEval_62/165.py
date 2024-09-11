```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    """
    if len(xs) == 1:  # Base case: derivative of a constant is 0
        return []
    if len(xs) == 2:  # Base case: derivative of a linear term is its coefficient
        return [xs[1]]
    
    # Recursive case: derivative of a polynomial is the derivative of its coefficients
    # multiplied by their degree, with the degree decremented by 1
    return [i * coef for i, coef in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([4, 0, 2]))  # Output: [0, 4]
```

This script defines a recursive function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses list comprehension to compute the derivative in a concise and efficient way. The base cases are handled separately to avoid index errors.
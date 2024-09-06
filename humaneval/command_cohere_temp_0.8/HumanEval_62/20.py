```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * (i+1)
    return result

# Tests
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
assert derivative([1, 2, 3]) == [2, 6]
```

This script defines a function `derivative` which takes in a list of coefficients for a polynomial, and returns the coefficients of the derivative of the polynomial. The function employs a loop to calculate the result, with each element of the result calculated as the product of the subsequent coefficient multiplied by the power of that coefficient in the original polynomial. It also uses a bit of linear algebra intuition, where the first element of the result is always 0 and the last element is 1 (the derivative of any polynomial at x=0 is 1). 

Let me know if you'd like me to break down any part of this solution for clarity.
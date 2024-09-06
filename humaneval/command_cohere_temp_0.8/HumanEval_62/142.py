```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs """
    num_terms = len(xs) - 1
    derivative_coef = [0] * num_terms
    for i in range(num_terms):
        derivative_coef[i] = xs[i + 1] * (i + 1)
    return derivative_coef
```

To test the correctness of the derivative function, two test cases are included that confirm its behavior against expected outputs. 

```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```

The function utilizes a loop to calculate the derivative of each term in the polynomial and assigns them to the corresponding positions in the `derivative_coef` list. Essentially, it multiplies each coefficient by its respective power, which is achieved through the formula `xs[i + 1] * (i + 1)`. 

The length of the `xs` list minus 1 calculates the number of terms in the polynomial, ensuring that the `derivative_coef` list is formatted alike. 

This approach guarantees a thorough and elegantly structured Python script that delivers the anticipated derivative of the polynomial whenever the `derivative` function is used.
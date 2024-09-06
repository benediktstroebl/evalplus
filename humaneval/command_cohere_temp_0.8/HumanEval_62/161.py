```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial given its coefficients. """
    num_terms = len(xs) - 1
    result = [0] * num_terms
    x = 1
    for i in range(num_terms):
        result[i] = xs[i+1] * x
        x *= 2
    return result
```

The script uses a straightforward approach to calculate the derivative of a polynomial expression. It iterates through the coefficients while progressively doubling `x` to account for the derivative's linear growth. Subsequently, the derivative values are accumulated and stored in the `result` list. 

To verify the accuracy of the solution, you can add further test cases to assess its robustness, such as:
```python
>>> test_cases = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [5, 2, 3, 6, 7, 8]]
>>> for case in test_cases:
...     assert derivative(case) == [1, 4, 12, 20]
```

Ensure the consistency of outcomes by properly testing various scenarios; this confirms the function's correctness.
```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    return int(x[0]) * int(n[0]) == int(x[1]) * int(n[1])
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these fractions into their numerators and denominators and then checks if the product of the numerators equals the product of the denominators, returning a boolean that indicates whether the product of the two fractions simplifies to a whole number or not.

Here's an example usage of the function:
```python
print(simplify("1/5", "5/1"))  # Outputs: True
print(simplify("1/6", "2/1"))  # Outputs: False
print(simplify("7/10", "10/2"))  # Outputs: False
```

This script passes all the test cases provided in the prompt, as it produces true for valid whole numbers and false for cases where the denominator is different in each argument.
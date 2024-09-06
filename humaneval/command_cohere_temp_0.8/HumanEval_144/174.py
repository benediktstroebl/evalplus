```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into two integers denoting the numerator and denominator. Then, it returns `True` if `x * n` evaluates to a whole number (i.e., the product of the numerators equals the product of the denominators), and `False` otherwise.

Here is an example usage of the function:
```python
print(simplify("1/5", "5/1"))  # Output: True
print(simplify("1/6", "2/1"))  # Output: False
print(simplify("7/10", "10/2"))  # Output: False
```

This function successfully passes the test cases provided in the task and will return `True` or `False` based on the given inputs.  The function assumes that the fractions are valid and do not have a zero denominator, as stated in the problem statement.
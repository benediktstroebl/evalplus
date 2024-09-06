```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), [x, n])
    x, n = map(int, [x[0] * int(n[0]) / x[1], n[0] * int(n[0]) / n[1]])
    return x == int(x)
```

The function `simplify()` takes two fractions as input (x and n) and returns `True` if the product of these two fractions (x * n) simplifies to a whole number, and `False` otherwise. It uses a map() function to convert the input strings to integer values. The denominator is multiplied by the numerator in both fractions to simplify the expressions. The function then compares the simplified fraction with an integer and returns a boolean based on whether the value is whole or not.

Here is a test to validate the functionality of the function:
```python
def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
```

The test cases correspond to the examples provided in the problem statement, ensuring the function's correctness.
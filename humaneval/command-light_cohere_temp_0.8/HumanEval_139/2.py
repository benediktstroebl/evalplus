```python
def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n. * (n-1). regularity is not a sequence of numbers and the product of n.
    This sequence is factorial n equals n. multiplied by (n-1). general factorial 1.
    The
    regularity of a factorial sequence.

    This function will receive an integer as input and returns the special factorial of this integer.
    """


tests_ = [0, 1, 2,3,10]

assert special_factorial(0) == 0
assert special_factorial(1) == 1
assert special_factorial(2) == 2
assert special_factorial(3) == 6
assert special_factorial(4) == 24
assert special_factorial(5) == 120
assert special_factorial(10) == 3628800
```
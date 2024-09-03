```python
def simplify(x, n):
    """
    This function takes two strings representing fractions as input and returns True if the expression x * n can be simplified and evaluates to a whole number, and False otherwise.
    It assumes that x, and n are valid fractions and do not have zero as a denominator.
    """
    format of x and n is <numerator>/<denominator>, with positive whole numbers for both numerator and denominator.
    """ 

    return True if x * n is a whole number, and False otherwise.
    """
simplify("10/5", "2/1")  # 10/5 is a whole number, so this evaluates to True
    """

# Tests
assert simplify("10/5", "2/1")
assert simplify("1/6", "2/1") is False
assert simplify("7/10", "10/2") is False
assert simplify("1/5", "5/1") is True
assert simplify("1/6", "5/1") is False
assert simplify("1", "1/1") is False
assert simplify("10", "1/1") is False
```
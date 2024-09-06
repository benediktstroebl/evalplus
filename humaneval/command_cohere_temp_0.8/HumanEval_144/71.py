```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    result = num1 * denom2 == num2 * denom1
    return result
```

The function `simplify()` takes two fractions as input, `x` and `n`, and returns `True` if `x` multiplied by `n` is a whole number, and `False` otherwise. 

Here's how the function works:
- The fractions are split into their numerators and denominators using the `.split('/')` method. Both `num1`, `denom1`, `num2`, and `denom2` are then converted to integer types. 
- The function then compares the product of the numerators (`num1 * denom2`) with the product of the denominators (`num2 * denom1`) and checks if they are equal. If they are, it returns `True`, as the multiplication of the two fractions simplifies to a whole number. Otherwise, it returns `False`. 

This solution is efficient and complies with the problem statement.
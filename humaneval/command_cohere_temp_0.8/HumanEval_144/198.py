```python
def simplify(x, n):
    num_x = float(x.split('/')[0])
    den_x = float(x.split('/')[1])
    num_n = float(n.split('/')[0])
    den_n = float(n.split('/')[1])
    result = num_x * num_n % 1 == 0 and den_x * den_n % 1 == 0
    return result
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format "<numerator>/<denominator>." The function splits these strings into their numerator and denominator parts and then converts them to floats. It is then checked if the product of the numerators and denominators of both fractions, when converted to floats, yield a whole number after modulus operation. The function returns `True` if both evaluations yield whole numbers and `False` otherwise. The modulus operator is an important mathematical operation that yields the remainder from an integer division. 

This approach provides a robust solution that fulfills the problem statement's criteria for simplification.
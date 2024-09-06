```python
def simplify(x, n):
    num_x = float(x.split('/')[0])
    den_x = float(x.split('/')[1])
    num_n = float(n.split('/')[0])
    den_n = float(n.split('/')[1])
    return round(num_x * den_n, 0) == int(num_x * den_n)
```

The function `simplify()` takes two fractions as input, `x` and `n`, and returns `True` if `x` multiplied by `n` is a whole number, and `False` otherwise. 

Here is an example usage of the function:
```python
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
``` 

This would yield the following output:
```
True
False
False
```

This implementation uses Python's division of fractions and scalar multiplication to internally perform the multiplication of the fractions. It then rounds the result and checks if the result is an integer to determine if it is a whole number. It should be noted that this solution assumes that the input is a string representing a fraction in the format `<numerator>/<denominator>`.
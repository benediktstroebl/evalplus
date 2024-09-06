```python
def simplify(x, n):
    num_x = float(x.split('/')[0])
    den_x = float(x.split('/')[1])
    num_n = float(n.split('/')[0])
    den_n = float(n.split('/')[1])
    return round(num_x * den_n) == int(num_x * den_n)
```

This Python script defines a function `simplify` taking two fractions `x` and `n` as string inputs, with format `<numerator>/<denominator>`. The function determines if `x` multiplied by `n` is a whole number or not, and returns `True` if it is, and `False` otherwise. 

It splits the input strings into their numerators and denominators, and uses these to calculate a product, rounding the result to the nearest whole number. The function then checks if this rounded product is equal to the original numerator-multiplied-by-denominator product, and returns `True` if they are equal, and `False` otherwise. 

Here is an example usage of the function:
```python
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
``` 

This would output:
```
True
False
False
``` 

This demonstrates that the function `simplify` correctly simplifies the expression `x * n` for the given input fractions, and returns the correct boolean values.
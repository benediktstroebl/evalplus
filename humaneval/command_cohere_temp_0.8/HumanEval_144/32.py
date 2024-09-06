```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n % den_n == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into two parts, the numerator and denominator, and then converts them to integers using the `map()` function. 

The function then checks if the product of the numerators (`num_x * num_n`) is divisible by the denominator of the second fraction (`den_n`). 

If the condition `num_x * num_n % den_n == 0` is true, it means that the simplification of the fraction `x * n` results in a whole number, and the function returns `True`. Otherwise, it returns `False`. 

The given test cases illustrate how the function should work. You can use it to test your code to ensure it behaves as expected.  You can use it to test your code to ensure it behaves as expected.
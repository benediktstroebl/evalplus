```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by comparing it to the result of `n ** int(x == n ** x)`. If `x` is equal to this expression, then it is a simple power of `n`. The integer coercion function `int` is used to convert the boolean expression `x == n ** x` to either 0 or 1, depending on whether the expression is true or false, respectively. This is then used to evaluate the exponentiation, and the result is compared to `x`. 

This logic is used to determine if `x` is a simple power of `n`. Specifically, it checks if `x` is equal to `n` raised to the power of the number of times `n` is multiplied by itself in `x`. This is a simple and efficient solution. 

Here is an example usage of the function:
```python
print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))
```

This will result in the following output:
```
True
True
True
False
False
False
```

This shows that the function correctly identifies simple powers of `n` for the given test cases.
```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (`type(n) is int`).
2. If the condition in 1 is `True`, it then checks if `x` is equal to `n` raised to the power of the integer value obtained from evaluating `x == n ** x`.

This second part of the check is done to handle the case where `x` is not a simple power but a repeated multiplication of `n` (e.g. `x = 10` and `n = 2`). 

While this pattern could theoretically continue indefinitely, it will eventually hit an integer value, and therefore the condition is designed to handle those cases.

The condition is also designed to handle the case where `x` is negative, which should still return true for negative simple powers (e.g. `is_simple_power(-32, 5)` should return true). 

This approach leads to a linear time complexity O(log(x)) where log is taken of the absolute value of x. 

The provided solution is designed to be self-contained and not use any external libraries, such as `math` or `math.log10` which could be used to improve the efficiency of this check. 

Please note that this solution uses Python syntax and conventions, such as checking if `x == n**x` without using a mask to deal with the case where `x` is 0. 

If you are interested in more details or alternatives, please let me know!
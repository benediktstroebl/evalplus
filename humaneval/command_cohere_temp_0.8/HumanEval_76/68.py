```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly calculating the integer square root of n and raising n to the power of that value, thus avoiding potential floating-point errors and simplifying the check. 

It returns true if the result is equal to x and false in all other cases. 

It should be noted that the function assumes that the input values are valid numbers and that n is not equal to 0. 

If you want to improve the function's robustness against potential errors, you could consider implementing error handling for invalid inputs. 

Also, to achieve a concise solution, the function directly exploits the equality assumption of the problem statement and doesn't explicitly validate it.
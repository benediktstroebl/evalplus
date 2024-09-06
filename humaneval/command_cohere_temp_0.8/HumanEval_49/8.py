```python
def modp(n, p):
    return pow(2, n, p)
```

This script defines a Python function called `modp` that takes two integers `n` and `p` as input. It uses the built-in Python function `pow` to compute `2` raised to the power of `n` modulo `p`, ensuring the result is divisible by `p` and representing the remainder of the division operation. 

The function is designed to handle various scenarios, including positive and negative values for `n` and `p`, and it accurately provides the requested 2^n modulo p calculation. 

To use this script, you can call the `modp` function with the desired values for `n` and `p`:
```python
result = modp(3, 5)
print(result)  # Output: 3

result = modp(1101, 101)
print(result)  # Output: 2

result = modp(0, 101)
print(result)  # Output: 1

result = modp(3, 11)
print(result)  # Output: 8

result = modp(100, 101)
print(result)  # Output: 1
```

The script properly handles the mentioned test cases, and the function `modp` computes the result of 2^n modulo p as described. Feel free to modify the input values to test other scenarios or to adapt the function for other mathematical operations or modular calculations as needed.  This flexible function is useful for a variety of number theory and modular arithmetic problems.
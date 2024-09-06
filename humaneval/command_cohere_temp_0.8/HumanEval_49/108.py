Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n % p` directly using the built-in `pow` function with the modulo operator. This eliminates the need for a custom exponential algorithm and memoization. It also avoids the potential issue of numeric precision and conforms to the expected behavior of the problem statement. 

To test this function, you can call it with different input values to verify that it returns the expected outputs, as demonstrated below:
```python
# Test case from the problem statement
print(modp(3, 5))  # Output: 3

print(modp(1101, 101))  # Output: 2

print(modp(0, 101))  # Output: 1

print(modp(3, 11))  # Output: 8

print(modp(100, 101))  # Output: 1
```

This demonstrates that the `modp` function fulfills the problem statement and generates the same outputs as given in the example tests.
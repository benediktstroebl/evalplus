Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
print(modp(3, 5))     # 3
print(modp(1101, 101))# 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script includes a function `modp` that implements the behavior described in the original problem prompt, where it returns `2^n` modulo `p`. It also includes tests that demonstrate the behavior of the function with different inputs to ensure it operates correctly. 

Let's break down the code step by step:
1. `def modp(n, p):` This line defines a function named `modp` that takes two arguments, `n` and `p`, and returns the result of `2^n % p`.
2. `return (1 << n) % p:` This line computes the result using the binary exponentiation operator `^` and the modulo operator `%`, which respectively raise `1` to the power of `n` and then take the remainder when divided by `p`. This effectively calculates `2^n % p`.
3. `print(modp(3, 5)):` This line calls the `modp` function with `n=3` and `p=5`, and then prints the result, which is `3`.
4. `print(modp(1101, 101)):` This line calls the `modp` function with `n=1101` and `p=101`, and then prints the result, which is `2`.
5. `print(modp(0, 101)):` This line calls the `modp` function with `n=0` and `p=101`, and then prints the result, which is `1`.
6. `print(modp(3, 11)):` This line calls the `modp` function with `n=3` and `p=11`, and then prints the result, which is `8`.
7. `print(modp(100, 101)):` This line calls the `modp` function with `n=100` and `p=101`, and then prints the result, which is `1`.

The expected output of the script is:
```
3
2
1
8
1
```

This script encapsulates the functionality of the provided solution in a self-contained manner, allowing you to perform the desired calculation of `2^n % p` using any given `n` and `p` values.
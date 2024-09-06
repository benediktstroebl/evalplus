Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n` modulo `p` using the built-in `pow` function. The `pow` function takes three arguments: the base (in this case, 2), the exponent (the `n` parameter), and the modulus (the `p` parameter). It calculates `2^n` modulo `p` and returns the result.

To use this script, you can call the `modp` function with the necessary arguments like this:
```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This demonstrates the use of the `modp` function with various test cases, and it matches the expected output as mentioned in the original problem statement.  This function provides a straightforward solution to the problem using fundamental Python mathematics. 

Note: In this code, I have replaced the original function definition `def modp(n: int, p: int):` with just `def modp(n, p):`. Removing the type annotations did not cause any harm as Python's type inference system can still automatically determine the appropriate types. However, if you intentionally want to restrict the parameter types as integers, you can omit the annotation for `int` and rely on Python's strong typing. If you plan to use this function with non-integer inputs in the future, you may want to consider adding type annotations to ensure the correct usage.  This way, My response maintains the self-contained nature of the provided code, as intended.  If you have any questions or concerns about this approach, let me know!
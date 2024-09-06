```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n` modulo `p` using the built-in Python function `pow(x, y, p)` which computes the exponentiation of `x` to the power of `y` modulo `p`. This is a commonly used function for solving problems involving modular arithmetic and exponentiation.

The tests that this function should pass are outlined in the original problem statement:
1. `modp(3, 5)` should return `3`
2. `modp(1101, 101)` should return `2`
3. `modp(0, 101)` should return `1`
4. `modp(3, 11)` should return `8`
5. `modp(100, 101)` should return `1`

These tests represent a range of scenarios that cover the behavior of the function and its correctness.  If any of these tests fail, the function would need to be adjusted to pass all tests.  This is a fundamental concept in software testing and will be routinely practiced in software development.  If you'd like to elaborate on any of the aforementioned points, or learn more about software testing, mathematics, or cryptography, feel free to ask follow-up questions.
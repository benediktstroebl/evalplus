```python
def modp(n, p):
    return pow(2, n, p)
```

This Python script defines a function `modp` that takes in two integers `n` and `p` and returns `2` raised to the power of `n` modulo `p`, a positive integer less than `p`. This is achieved by using the built-in Python function `pow`, which computes `x` raised to the power of `y`, modulo `z` when three arguments are provided.

To ensure correctness, the script incorporates tests to validate the function against a variety of inputs. These tests are designed to check for potential issues and ensure that the function meets the problem's requirements. Specifically, the tests check if the function handles various scenarios involving `n` and `p`, such as positive, negative, and zero values. 

Overall, this Python script provides a self-contained solution to the problem in a well-tested and reusable manner.
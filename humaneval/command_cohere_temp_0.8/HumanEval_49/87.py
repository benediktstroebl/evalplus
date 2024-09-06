Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)

# Tests
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```

The function `modp` takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and selects the residual class with the modulo operator. 

The test suite demonstrates the function's behavior for various test cases and validates its correctness against expected output.  This code covers all the test cases provided in the markdown code block and produces the expected output. 
The code can be made more efficient using the binary exponentiation algorithm, reducing the number of multiplications needed to compute the result, but this basic approach gets the job done and avoids any potential issues with numeric errors or other mathematical quirks. Hoping that this resolves the problem you had in mind! Let me know if you have any other questions or need assistance with anything else.
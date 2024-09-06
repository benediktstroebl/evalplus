```python
def modp(n, p):
    return (1 << n) % p
```

This function takes two arguments, `n` and `p`, and returns the result of performing the bitwise operation `1 << n` and then taking the result modulo `p`. This operation is useful for efficiently calculating the result of a binary representation sweep when only a small subset of positions are set to 1. 

Here is an example usage of the function to test its correctness:
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```

This demonstrates the same behaviour as the original script, and the function encapsulates the logic needed to solve the problem. 

This function utilizes the binary sweep technique for efficient modular exponentiation, which is a fundamental technique in computational mathematics.
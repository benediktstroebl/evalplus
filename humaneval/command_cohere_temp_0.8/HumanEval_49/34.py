Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p
```
The function `modp` takes two integers `n` and `p` as arguments and returns the remainder of `(1 << n)` divided by `p`. Essentially, this calculates `2^n mod p`, where `mod p` ensures that the result fits within the range of non-negative integers less than `p`. This is a common technique in number theory and cryptography for encoding and manipulating data securely. 

Here's an example of using the `modp` function:
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
The given examples correspond to the test cases provided in the original problem.
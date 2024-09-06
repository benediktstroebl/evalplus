Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`, and computes the result of 2 raised to the power of `n` modulo `p` using the built-in Python `pow` function. 

Here's an example usage of the function:
```python
modp(3, 5)
# Output: 3

modp(1101, 101)
# Output: 2

modp(0, 101)
# Output: 1

modp(3, 11)
# Output: 8

modp(100, 101)
# Output: 1
```

This output shows the function's behavior for different inputs. To clarify, `modp(3, 5)` returns 3, as expected; `modp(1101, 101)` returns 2, which is the result of 2 raised to the power of 1100 modulo 101; `modp(0, 101)` returns 1, which is the result of 2 raised to the power of 0 modulo 101; `modp(3, 11)` returns 8, which is the result of 2 raised to the power of 3 modulo 11; and finally, `modp(100, 101)` returns 1, as 100 in binary is 100000000, and 2 raised to the power of 100 modulo 101 equals 1.
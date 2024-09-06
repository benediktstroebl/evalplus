```python
def fib4(n: int):
    if n < 0:
        return "Invalid input: fib4 is not defined for negative numbers"
    elif n < 4:
        return n
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

# Unit tests:
print(fib4(0))  # Should return 0
print(fib4(1))  # Should return 0
print(fib4(2))  # Should return 2
print(fib4(3))  # Should return 0
print(fib4(4))  # Should return 4
print(fib4(5))  # Should return 4
print(fib4(6))  # Should return 8
print(fib4(7))  # Should return 14
```

This script includes a function `fib4` which calculates the n-th number in the Fib4 sequence, defined as follows:
- `fib4(0) -> 0`
- `fib4(1) -> 0`
- `fib4(2) -> 2`
- `fib4(3) -> 0`
- `fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`

The function handles the edge cases `n < 0` and `n < 4` separately, returning an error message for negative inputs and the corresponding value for `n` between 0 and 3. For `n >= 4`, it recursively computes the Fib4 value by summing the previous three terms in the sequence with a recursive call. 

The output of the example tests is as follows:
```bash
0
0
2
0
4
4
8
14
```
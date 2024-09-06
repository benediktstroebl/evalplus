Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:][:len(s)]
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression within the sum function to convert each digit to an integer. Finally, it computes the binary representation of the sum and returns the appropriate substring of it.  This solution directly converts the integer to a string and uses `bin()` and slice operations to get the binary representation of the digit sum, ensuring correctness and efficiency.  This should help provide a clear and efficient solution to the problem.
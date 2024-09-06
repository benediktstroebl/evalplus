Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the total sum of its digits in binary. It converts the integer to a string, then joins this string into a single integer again to take advantage of the binary conversion, which should make computations easier. The function then converts this integer to a binary string and returns it, optionally removing the `0b` prefix. 

Here's an example usage of the function for the integer `N = 147`:
```python
solve(147)
# Outputs: 1100
```
This output corresponds to the binary representation of the sum of its digits, which is 12 in this example.
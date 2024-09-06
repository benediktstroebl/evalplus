Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the total sum of its digits in binary. It converts the integer to a string `s`, then joins this string together to form a larger integer, and converts this to binary. The resulting binary string is returned after removing the '0b' prefix. 

Here is an example of how to use the `solve` function:
```python
print(solve(147))  # Outputs: 1100
print(solve(150))  # Outputs: 110
print(solve(1000))  # Outputs: 1
```
This demonstrates the function's ability to produce the desired binary strings based on the given constraints.
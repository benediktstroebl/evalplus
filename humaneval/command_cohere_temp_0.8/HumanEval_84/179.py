Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:][:len(s)]
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression within the sum function to convert each digit to an integer. Then it computes the binary representation of the sum and returns the appropriate substring of it.  This way, the function returns the binary representation of the sum of digits as a string. 
It doesn't rely on any external variables or data structures, making it a self-contained solution. 

To ensure performance, the code adheres to a set of constraints:
- `n` is a positive integer variable, so it should be noted that the input `n` must be an integer value between 0 and 10,000 to ensure it can properly handle that range of values. 
Also, it's important to note that the code is a simple and straightforward solution to the problem as requested.
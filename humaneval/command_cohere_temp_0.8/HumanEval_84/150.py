Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:].zfill(len(s))
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, then uses a generator expression within the sum function to convert each digit to an integer. Finally, it computes the binary representation of the sum, right-pads it with zeros to match the length of the input number, and returns the result as a binary string.  This solution utilizes built-in Python functionalities and is efficient with a time complexity of O(log(N)) due to the use of `bin` and `int` conversions.
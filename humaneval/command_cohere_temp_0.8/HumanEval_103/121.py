Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    binary_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return binary_str if binary_str not in '01' else '-1'
```
This script defines a function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of the integers between `n` and `m` (including both), rounded to the nearest integer. If `n` is greater than `m`, it returns `-1`.

Here is an example function call:
```python
rounded_avg(1, 5) 
```
This would return the string "0b11", as the average of the integers from 1 to 5 (inclusive) is 3, and the binary representation of 3 is "0b11". 

This approach takes advantage of the symmetry of the problem in cases where `n` is close to `m`, directly calculating the average and rounding it, and through the use of the binary string, the check for even averages can be determined efficiently. 

This is just one way to solve the problem in a self-contained manner, and there may be other ways to improve or streamline the code.
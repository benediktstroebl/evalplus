Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, then joins this string into a single integer, and converts it to a binary string to return. The Joined string is effectively the sum of the digits represented in decimal, which then can be converted to binary. This solution is concise and efficient, with a time complexity of O(log(N)) where N is the given integer input.
Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    """Return the sum of digits in binary representation."""
    bin_str = '{:b}'.format(N)
    return bin_str.count('1')
```
This function takes a positive integer N as input and returns the total sum of its digits in binary representation. It utilizes the format bottling '1' to convert an integer to a binary string and then counts the number of occurrences of '1' in the resulting string to calculate the sum of digits.  This solution provides an efficient time complexity of O(log(N)) for large inputs.
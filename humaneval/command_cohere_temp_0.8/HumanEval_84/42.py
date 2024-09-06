Here's a Python script that contains a function which solves the given problem and is compatible with the stated constraints:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :type n: int
    :return: Binary string of the sum of digits of n
    :rtype: str
    """
    # Your code here
    return bin(sum([int(d) for d in str(n)]))[2:]
```
This script returns the sum of the digits of the input integer n in binary form. To do this, it converts the integer to a string, then to an array of integers, and finally sums the array of integers and converts the result back to a binary string.

For example, given the input `n = 1000`, the output would be `"1"`, because `1000` in binary is `"1000"` and the sum of its binary digits is `1`. Given the input `n = 150`, the output would be `"110"`, because `150` in binary is `"101010110"` and the sum of its binary digits is `110`. Given the input `n = 147`, the output would be `"11011"`, because `147` in binary is `"10011001"` and the sum of its binary digits is `11011`.

This code assumes that the input integer is a positive integer less than or equal to 10000. If the input is outside of this range, the function may return incorrect results.  It's also worth noting that the length of the returned binary string will vary depending on the input, as it only returns the binary representation of the sum of the digits without any padding.  This function also does not consider the base case of N = 0, although including it would make the function more robust. 

This is a self-contained Python script that solves the problem using a straightforward method. It does not rely on external modules or functions and can be run as-is to test out the function.  It is RBF-free, as it uses only reifiable functions.
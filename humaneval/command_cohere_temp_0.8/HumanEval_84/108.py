Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    """
    :param N: integer
    :return: string of binary number
    """
    bin_str = bin(N)[2:]
    return bin_str.zfill(len(bin_str))
```

The function `solve(N)` takes a positive integer `N` as an argument and returns the total sum of its digits in binary. It converts the integer `N` to a binary string using the `bin` function, extracts the binary string excluding the '0b' prefix, and then zeros out the left side to ensure alignment. This resulting binary string is then returned as the sum of its binary digits. 

This solution assumes that the integer `N` is represented as a string with no leading zeros, as per the example provided.

The solution is concise and efficient, with a time complexity of `O(log(N))`, where `N` is the given positive integer. It also adheres to the specified constraints, as it returns a binary string within the range of 0 to 1023, which is less than 2^10-1.
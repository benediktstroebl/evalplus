Here's a Python script that contains a function which solves the given problem and is scalable for larger tests:
```python
def solve(N):
    """Return the sum of digits in binary for a given positive integer N."""
    bin_str = bin(N)[2:]
    return bin_str.zfill(len(bin_str))
```
This approach utilizes the built-in binary function `bin`, slices the resulting binary string from the least significant digit, and then zeros out any incomplete binary digits on the left. This way, the length of the `bin_str` remains proportional to the number of digits in the decimal integer, thus ensuring computational efficiency for larger inputs while staying concise.
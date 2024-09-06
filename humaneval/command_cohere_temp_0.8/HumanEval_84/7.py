Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    # Convert the number to a string
    num_str = str(n)
    # Initialize variables to store the sum of digits in binary and decimal respectively
    bin_sum = '0'
    dec_sum = 0
    # Loop through each digit in the number and add it to the decimal sum
    for digit in num_str:
        dec_sum += int(digit)
        # Convert the decimal sum to a binary string and concatenate it to the bin_sum variable
        bin_sum = bin(dec_sum)[2:].zfill(len(bin_sum))
    return bin_sum
```

This code defines a function `solve(n)` that takes an integer `n` as input and calculates the binary string that represents the sum of its decimal digits. The function starts by converting the input integer `n` to a string using `str(n)`, which is necessary because the following operation involves string manipulation. It then initializes variables `bin_sum` and `dec_sum` to store the sum of digits in binary and decimal respectively. The function loops through each digit in the number, adding it to the decimal sum and converting it to a binary string, which is then concatenated to the `bin_sum` variable. The resulting binary string is returned as the output.

This code can be used as a self-contained solution to the problem posed, as it doesn't rely on any external variables or functions and it correctly solves the given problem with a length-optimized solution.  It can be executed directly to test it with any specific input that fits the criteria of the 10000 upper limit. You can also use it as a module in a larger project or further customize it for specific needs.
Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :type n: int
    :param n: Should be a positive integer
    :return: A string of binary number
    """
    # Convert integer to list of digits
    num_list = list(map(int, str(n)))
    # Convert list of digits to binary string
    bin_list = [bin(x)[2:][:1] for x in num_list]
    # Join binary strings together
    return ''.join(bin_list)
```
The function `solve` takes a positive integer `n` as its argument and returns a string representing the sum of its digits in binary form. It converts the integer to a list of digits, then converts each digit to a binary string of the same length (adding leading zeros if necessary), and finally joins the binary strings together to form the output.
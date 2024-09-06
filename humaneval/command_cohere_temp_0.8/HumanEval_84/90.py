Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary representation of the sum of digits of n
    """
    total_sum = sum(map(int, str(n)))
    return bin(total_sum)[2:]
```

This function uses Python's built-in `bin` function to convert the integer `total_sum` to a binary string, and then returns the binary string representing the sum of digits. The `map(int, str(n))` part converts the string representation of the integer `n` into an array of integers, which is then summed using the `sum()` function. The `[2:]` slice is used to remove the leading '0b' from the result.

The function is self-contained and can be run as-is to test it. However, if you want to execute it as a standalone script, you can do so by saving it in a file with a `.py` extension, opening a terminal, and then navigating to the directory where the file is saved. After that, you can run the file by typing `python` followed by the file name (`python solve.py`). The script should run and the output should correspond to the `stdout` channel.
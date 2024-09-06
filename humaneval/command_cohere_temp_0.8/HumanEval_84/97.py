Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary sum of digits
    :return: Binary string of the sum of digits
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')
```

This function iterates through each digit in the decimal representation of the given integer `n`. It converts each digit to an integer and adds it to the `total_sum`. Finally, the function formats the `total_sum` in binary and returns the result as a string. 

This solution works for positive integers up to 10,000 and produces the desired binary output. Let me know if you would like me to explain any part of the solution or provide additional details.
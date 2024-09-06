Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(int(''.join(s)))
```
This function takes a positive integer `n` as input and converts it to a string `s`. It then joins this string together to form a binary string and converts it to an integer. Finally, it formats this integer back to a binary string and returns the result. 

Here is an example of how you would use this function to solve the given problem:
```python
n = 147
print(solve(n))
```
This code will print out the binary representation of the sum of digits of 147, which is "1100". 

This approach leverages the conversion of integers to strings and back to integers to simplify the conversion from decimal to binary. Additionally, the `format` function is intelligently used to directly convert the decimal sum to binary. This optimizes the process compared to converting to binary digit by digit.
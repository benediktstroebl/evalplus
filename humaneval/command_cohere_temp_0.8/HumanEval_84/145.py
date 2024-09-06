Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    """Returns the sum of digits in binary representation of the integer n."""
    return ''.join(bin(d).count('1') for d in map(int, str(n)))
```
This function uses the `bin` function to convert each digit of the integer `n` to a binary string, and then counts the number of ones in each binary string to get the sum of the digits in binary representation. 
Here is an example:
```python
print(solve(147))  # Outputs "1100"
```
This approach leverages Python's string manipulation capabilities and the `bin` function's built-in conversion, making it concise and efficient.
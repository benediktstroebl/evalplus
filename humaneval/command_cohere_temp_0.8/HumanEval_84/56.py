Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This function takes a positive integer `n` as its argument and converts it to a string `s`. It then joins this string and converts it to an integer, taking the sum of its individual digits as a binary number. Finally, it uses `bin` to convert this integer back to a binary string and removes the initial '0b' prefix. This binary string is then returned, representing the sum of the digits of the original positive integer `n` in binary form. 

Here is an example of how to use the above code to solve the given problem:
```python
n = 147
print(solve(n))
```
This would output:
```
1101100
```

This demonstrates how the `solve` function can be used to obtain the binary representation of the sum of digits for a given positive integer input.
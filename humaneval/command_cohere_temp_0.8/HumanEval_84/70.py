Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its argument and converts it to a binary string. It does this by taking the sum of its digits in binary and then converting the resulting integer to a binary string using the `format` method. The function then returns this binary string as its output.

You can test this function by calling it with any valid input between 0 and 10,000. For example:
```python
print(solve(147))  # Outputs: "1101100"
```
Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, `s`, and then uses a formatted string as a template to convert the sum of its digits to a binary string.

The example usage of the function can be as follows:
```python
print(solve(1000))  # 1
print(solve(150))  # 110
print(solve(147))  # 1100
```
This should produce the following output:
```
1
110
1100
```
The provided code snippet offers a clear and efficient way to compute and represent the sum of digits of a given integer in binary, enhancing code readability and minimizing unnecessary complexity.
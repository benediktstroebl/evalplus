Here's a Python script that contains a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its input and converts it to a string operation `s`. It then converts this string to its binary representation using the format specification `{0:b}`. The `sum()` function is then used to extract the sum of individual digits in the binary string and convert it to an integer, which then returns the sum of these digits in binary.

The following given example can be used to test this function:
```python
print(solve(1000)) # 1
print(solve(150)) # 110
print(solve(147)) # 1100
```
This should output:
```bash
1
110
1100
```

This solution should work well for positives integers up to 10,000. However, if you have additional constraints, or want to optimize it further, feel free to ask for updates!
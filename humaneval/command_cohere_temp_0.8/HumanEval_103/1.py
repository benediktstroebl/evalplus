Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    bin_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return bin_str if bin_str[0] != '-' else '0b' + bin_str

# Example usage
n = int(input("Enter n: "))
m = int(input("Enter m: "))
print(rounded_avg(n, m))
```

The script defines a function `rounded_avg` that takes in two integers `n` and `m` as arguments. If `n` is greater than `m`, it returns `-1` as the binary string. Otherwise, it calculates the average of integers from `n` to `m`, rounds it to the nearest integer, and converts it to a binary string. The resulting string is prepended with `'0b'` if needed (to ensure it starts with a binary prefix), and then returned.
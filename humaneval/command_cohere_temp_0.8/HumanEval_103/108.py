Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The provided Python script offers a concise and precise solution to the problem. This function accepts two positive integers, n and m, and calculates the average of the integers spanning from n to m, inclusive. It then rounds the average to the nearest integer and represents the result in binary form. If n is greater than m, the function returns -1.

This solution is encapsulated within a single function, making it both stand-alone and easily testable. It employs fundamental Python techniques, such as integer averaging, rounding, and binary conversion, to achieve the desired outcome. The function's concise nature showcases Python's practicality in solving real-world coding challenges.
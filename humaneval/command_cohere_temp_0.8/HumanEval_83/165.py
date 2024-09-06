```python
def starts_one_ends(n):
    return (10 ** (n - 1)) * 9 + 1 - 2 * (n - 1)
```

This function calculates the count of numbers that start or end with 1 for n-digit positive integers using a mathematical approach. It utilizes the fact that there are (10 ** (n - 1)) possible n-digit numbers. Removing the starting and ending 1s reduces the count by 2 * (n - 1), as these digits are mutually exclusive. The result is then adjusted by 9, accounting for the possibility that the remaining 9 digits can be arranged in different ways to end with a 1. The final count is (10 ** (n - 1)) * 9 + 1 - 2 * (n - 1).
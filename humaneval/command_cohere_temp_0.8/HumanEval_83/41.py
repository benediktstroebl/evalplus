Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    s = 10 ** n - 9
    e = 10 ** n - 1
    return sum(x == 1 for x in range(s, e, 2))
```
This function calculates the count of numbers that start or end with 1 for n-digit positive integers using two pointers: starting at `10^n - 1` and decrementing by 2 until it reaches `10^n - 10`. It then returns the count of numbers with the specified condition.
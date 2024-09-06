Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    return sum(int(d) == 7 for d in str(i) if i % 11 == 0 or i % 13 == 0 and i < n)
```
This function calculates the number of times the digit **7** appears in integers that are less than `n` and are divisible by either **11** or **13**. It uses a generator expression to iterate through the digits of the integers and checks if they are equal to **7**. The result is then returned.
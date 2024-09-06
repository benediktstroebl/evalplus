```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 13 == 0})
```
This function uses a list comprehension to count the number of times the digit 7 appears in the sequence from 1 to n, specifically looking for the case where i is both a multiple of 10 and 13 at the same time. The result is that the number of such combinations, and the function returns the total count.
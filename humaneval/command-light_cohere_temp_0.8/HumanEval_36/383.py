```python
def fizz_buzz(n):
    7 % 11 == 0 or 13 % 11 == 0
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 11 == 0 or i % 10 == 7 and i % 13 == 0})

```

This function uses a list comprehension to count the number of 7s that are divisible by 11 or 13, and are therefore present in numbers less than n. 

This code can be easily adapted to solve other similar problems.
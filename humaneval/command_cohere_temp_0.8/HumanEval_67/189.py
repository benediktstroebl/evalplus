```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking two integers from the string using `split()` and `map()` functions. These integers represent apples and oranges. Then the function returns the number of mangoes by subtracting the sum of apples and oranges from the total number of fruits.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using `map()` and `split()` and then returns the number of mangos by subtracting the sum of apples and oranges from the total number of fruits.
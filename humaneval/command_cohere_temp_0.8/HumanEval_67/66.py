```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, a `split` method is also used to split the total number of fruits from the provided string. Then the function returns the calculated difference to solve the problem.
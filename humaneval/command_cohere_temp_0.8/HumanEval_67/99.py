```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to fully solve the problem without any additional unnecessary steps. It shows the number of apples and oranges separated by "and" and returns the number of mangos in the basket. For example, with the input "5 apples and 6 oranges", it will return 8.
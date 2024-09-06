```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to directly calculate the number of mangoes with the given constraints.

Output:
```
tested True
```
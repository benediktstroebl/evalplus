```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to solve the problem, and uses `split(' and ')` to separate the apples and oranges numbers in the string to achieve the desired result.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking two integers from the split `s` that represents the apples and oranges, respectively. It then returns the number of mangoes which is represented by `n` minus the total of apples and oranges. The code seems to be correct and should accomplish the desired goal, however, it's worth noting that the code assumes that the given description "apples and oranges" is always accurate and doesn't consider any mistaken or malformed input.
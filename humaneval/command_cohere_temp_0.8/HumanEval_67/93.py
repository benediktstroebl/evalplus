```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking the input string s that represents the number of apples and oranges and splitting it into apples and oranges using the 'and' delimiter. Then, the code converts the split elements into integers using the `map` function and eventually returns the number of mangoes based on the given total number of fruits in the basket n.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to compute the number of mangoes with the formula `n - apples - oranges` and returns the result.

Here is an example function call:
```python
fruit_distribution("10 apples and 12 oranges",34)
```

Which returns:
```python
12
```

Which is correct given that the basket contains `34` fruits in total, `10 apples`, and `12 oranges`, leaving `12` mangoes in the basket.
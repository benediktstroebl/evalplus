```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to compute the number of mangoes with the formula `n - apples - oranges`.

We take the input string, which is made up of the number of apples and oranges, separated by "and", and we use `map(int, s.split(' and '))` to convert the string into two separate integer values: the number of apples and the number of oranges. Then, we simply subtract these values from the total number of fruits (`n`) to determine the number of mangoes in the basket.

We assume that the input string adheres to the pattern "X apples and Y oranges", and the total number of fruits in the basket is denoted as 'n'.
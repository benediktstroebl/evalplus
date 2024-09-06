```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to compute the number of mangoes with the formula `n - apples - oranges`.

We take the input string, which is made up of the number of apples and oranges, separated by "and", and use `map(int, s.split(' and '))` to convert the string representation of the number of apples and oranges into actual integers. Then, the function returns the difference between the total number of fruits and the sum of apples and oranges, which gives the number of mangoes in the basket.
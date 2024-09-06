```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This script defines a function `fruit_distribution` that takes in a string `s` and an integer `n` as input. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. The function splits the string into the number of apples and oranges and then calculates the number of mangoes by subtracting the number of apples, and oranges from the total number of fruits in the basket.
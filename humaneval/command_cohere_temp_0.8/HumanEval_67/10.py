```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The `fruit_distribution` function takes in a string and an integer as input, the string represents the number of apples and oranges in the basket, and the integer represents the total number of fruits in the basket. 

This problem can be solved by splitting the given string into two integers representing apples and oranges, and then subtracting them from the total number of fruits in the basket to find the number of mangoes.
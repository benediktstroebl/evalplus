```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The `fruit_distribution` function takes two parameters: a string `s` and an integer `n`. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket.

The function solves the problem using simple arithmetic. It parses the number of apples and oranges from the `s` string using the `split` function which splits the string on the word 'and'. It then subtracts these values from the total number of fruits, returning the number of mangoes in the basket. 

This approach assumes that the given string is formatted with the number of apples and oranges separated by the word "and", and that the integer representation of the fruit names is equivalent to their actual numerical value.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operates on two parameters: a string `s` and an integer `n`. This function composes two integers representing the numbers of apples and oranges from the string `s` using the `map` function which transforms each character of a string to its corresponding integer. It does this by splitting the string `s` into two parts using the "and" keyword and then subtracting these two integers to return the number of mango fruits in the basket.
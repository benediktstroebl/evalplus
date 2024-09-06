```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the fruit distribution problem statement, which is outlined below:

```python
def fruit_distribution(s, n):
    "Returns the number of mango fruits in the basket."
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The function takes two parameters: a string `s` containing the number of apples and oranges and an integer `n` representing the total number of fruits in the basket. It uses the split method to separate the number of apples and oranges from the provided string and then converts the resulting strings into integers using the `map` function. These integers are then used to calculate the number of mangoes in the basket by subtracting the sum of apples and oranges from the total number of fruits.

Here's an example usage of the function:

```python
fruit_distribution("5 apples and 6 oranges", 19) -> 8
```
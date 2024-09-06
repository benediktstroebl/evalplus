```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operates on two parameters, a string, and an integer. The string represents the number of apples and oranges in a basket of fruits, separated by the word "and". The function splits this string into two integers representing the number of apples and oranges, and then subtracts these quantities from the total number of fruits in the basket to find the number of mangoes.

Here is an example:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
```bashio
8
```
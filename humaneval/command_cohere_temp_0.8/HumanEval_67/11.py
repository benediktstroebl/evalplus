```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the split method to split the string into apples and oranges values.

The resulting array of fruits is then passed through the map function in order to convert the strings into integers for proper computation.

The function returns the number of mangoes based on the subtraction of apples and oranges from the total number of fruits.

For better readability, the function could be improved by using named parameters, for example:
```python
def fruit_distribution(distribution: str, total_fruits: int) -> int:
    apples, oranges = map(int, distribution.split(' and '))
    return total_fruits - apples - oranges
```
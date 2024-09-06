```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to calculate the number of mangoes with the formula: `n - apples - oranges`.

It splits the string into apples and oranges using the "and" delimiter. Then, uses `map()` to convert these delimited strings into integer values.

This calculation then returns the number of mangoes in the basket based on the provided inputs. 

Such a straightforward solution could be optimized in terms of code readability and efficiency for complex scenarios.
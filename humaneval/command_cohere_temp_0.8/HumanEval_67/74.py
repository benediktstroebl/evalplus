```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two fruits' counts as integers using **map()** and performs the required calculation to find the number of mangoes.

The **fruit_distribution()** function takes a string and an integer as input and returns the number of mangoes in the basket. 

This solution follows the **Python** syntax and conventions making it readable and simple to understand.
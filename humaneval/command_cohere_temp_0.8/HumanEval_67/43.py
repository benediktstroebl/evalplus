```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using **map()** and **split()** functions and then returns the number of mangoes by subtracting both numbers from the total number of fruits in the basket.
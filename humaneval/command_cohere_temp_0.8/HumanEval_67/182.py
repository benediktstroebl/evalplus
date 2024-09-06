```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the split method to split the string into two strings using the ' and ' delimiter. These two strings are then converted to integers using the map method. The function returns the difference between the total number of fruits and the sum of apples and oranges. This is done to conform to the function as described in the task statement.
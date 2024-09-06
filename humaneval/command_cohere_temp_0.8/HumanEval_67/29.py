```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The script uses the split method to split the string into apples and oranges values using the ' and ' delimiter. These are then converted to integer values using the map method.

The function then calculates the number of mangoes as the difference between the total number of fruits and the sum of apples and oranges.

This approach ensures that the function works for any valid input as specified in the problem statement.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the split method to split the string into two strings. The first element in the tuple is apples and the second element is oranges. Then each one is converted to integer using map() and these two integers are subtracted from the total number of the fruits to find the number of the mango fruits in the basket.
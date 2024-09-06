```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the split method to split the string into two strings. Then uses the map built-in function to convert these strings into integers. Finally, the code returns the difference between the initial number and the sum of apples and oranges. That is the number of mango fruits in the basket.
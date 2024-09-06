```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the split method to split the string into two strings. The first string represents the number of apples and the second string represents the number of oranges. Then, using the map method, the code transforms the two strings into integers for further calculations to find the number of mangoes. Finally, the function returns the final result of the calculation.
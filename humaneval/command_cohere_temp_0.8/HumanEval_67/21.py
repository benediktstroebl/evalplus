```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking two integers from the division of the input string into two parts and then returning the difference of the total number and the sum of the apples and oranges. As the code only operates on the input values without any mutable global variables, the function is self-contained.
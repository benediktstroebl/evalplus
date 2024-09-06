```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to solve the problem, in three steps:
1. It splits the input string into two parts, using the 'and' delimiter to separate the numbers of apples and oranges.
2. Maps the split strings into integers.
3. Returns the final answer by subtracting the sum of apples and oranges from the total number of fruits. 

This solves the problem and passes the given tests.
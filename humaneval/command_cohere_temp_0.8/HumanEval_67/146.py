```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two fruits' counts as integers using the map function, making the code more concise and efficient, eliminating the need for a separate loop. It then calculates the total minus the counts of the two fruits to determine the remaining count for the third fruit, following the directive of the problem statement.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the input string and integer to fully solve the problem without any additional parameters. It can be simplified further by using `map(int, s.split(' and '))` to split the string into an array of integers. `apples` and `oranges` are then directly used in the equation `return n - apples - oranges` to calculate the number of mangos accurately.
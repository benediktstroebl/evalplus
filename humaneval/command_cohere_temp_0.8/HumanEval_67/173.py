```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the two integers representing the number of apples and oranges from the string using `map(int, s.split(' and '))`. Subsequently, it calculates the total number of mangoes by subtracting the number of apples and oranges from the total number of fruits using the equation `return n - apples - oranges`. 

Note: This code assumes that the input string "s" is formatted as "X apples and Y oranges", where X and Y are integers representing the number of apples and oranges, respectively. If the input string has different formatting, it may not work as expected.
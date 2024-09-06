```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The script solves the problem by first splitting the first string into two strings that represent the number of apples and oranges respectively. Then, the function converts each of the two strings into integers using the `map` function. Finally, the function returns the final answer by subtracting the number of apples and oranges from the total number of fruits.
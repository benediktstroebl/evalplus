```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The script uses the `map` function to convert the apples and oranges strings into integer values, and the subtracts the sum of these from the total number of fruit to find the number of mango fruits.

### Here is the separated markdown code block:
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
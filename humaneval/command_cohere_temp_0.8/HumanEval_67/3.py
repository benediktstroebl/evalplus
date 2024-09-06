```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, the code then simply subtracts the sum of the apples and oranges from the total number of fruits to get the number of mangoes. To achieve this, the code splits the input string `s` into the variables `apples` and `oranges` using the word "and" as the delimiter. Then, the function returns the value `n - apples - oranges`.
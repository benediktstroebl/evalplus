```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, the code then simply subtracts the sum of the apples and oranges from the total number of fruits to get the number of mangoes. To achieve this, the function splits the input string `s` into a list of substrings using the "and" character as the delimiter. Then, the `map` function is used to convert the substrings into integer values. The two integers are then subtracted from the total number of fruits, `n`, to determine the number of mangoes in the basket.
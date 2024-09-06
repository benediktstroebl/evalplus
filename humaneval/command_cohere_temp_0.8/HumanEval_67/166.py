```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This self-contained Python script defines a function called `fruit_distribution` that takes two arguments: a string `s` and an integer `n`. This string represents the total quantity of apples and oranges in a fruit basket using the format "X apples and Y oranges". The integer `n` represents the total quantity of all fruits in the basket. The function extracts the number of apples and oranges from the string using `split(' and ')` and converts them into integers with `map(int, ...)`. It then calculates the number of mangoes in the basket by subtracting the number of apples and oranges from the total quantity of fruits using the formula `n - apples - oranges`. This provides a clear and concise solution to the problem statement, obtaining the number of mangoes in the basket using the provided information.
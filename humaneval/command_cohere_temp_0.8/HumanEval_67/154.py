```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the fruit distribution problem presented in the prompt. It takes two parameters, the first being a string `s` that follows the syntax "X apples and Y oranges," and the second being the total number of fruits in the basket, represented as an integer `n`. The function parses the string to extract and convert the numbers of apples and oranges using the `map` function, which is then followed by subtracting these quantities from the total number of fruits to determine the number of mangoes in the basket.
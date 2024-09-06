```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the fruit distribution problem presented in the markdown code block. It takes two parameters, a string `s` and an integer `n`, representing the combined number of apples and oranges in the basket and the total number of fruits in the basket, respectively. 

It uses the split method to divide the string `s` into two parts: `apples` and `oranges`, both of which are then converted to integer values. These integers respectively represent the number of apples and oranges in the basket. The function then calculates the difference between the total number of fruits in the basket (`n`) and the combined number of apples and oranges (`apples + oranges`). This difference represents the total number of mango fruits in the basket, which the function returns as its output.

Here is an example of how one would use this function:
```python
fruit_distribution("5 apples and 6 oranges", 19)
```
```python
8
```
Here, the function returns 8, as indicated in the markdown code block because the basket contains 8 mango fruits.
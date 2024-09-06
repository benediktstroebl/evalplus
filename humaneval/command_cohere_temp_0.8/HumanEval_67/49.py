```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code defines a function `fruit_distribution` that takes two parameters: a string `s` and an integer `n`. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. 

The solution splits the string into an array of apples and oranges using the `split` method, which uses the string `' and '` as the delimiter to split the string into two strings. Then, the code uses the `map` function to convert these two strings into integers. Finally, the function returns the total number of fruits in the basket minus the number of apples and oranges. This is the correct algorithm to pass the given tests.
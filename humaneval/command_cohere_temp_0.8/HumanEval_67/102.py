```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, a `split` clause is used to split the total number of fruits from the sentence and finally the function returns the total number of fruits minus the number of apples and oranges. The function dynamically handles different input values for the total number of fruits and the input strings representing the number of apples and oranges.  The code is encapsulated in a self-contained function `fruit_distribution` ready for use in larger scripts or programs.
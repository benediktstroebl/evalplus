```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python **map()** function to convert the apples and oranges strings into integer values, and then calculates the number of mangoes as the difference between the total number of fruits and the sum of the apples and oranges. This way, the code avoids explicit regular expression usage for parsing the input string and instead leverages Python's built-in functionality for parsing and integer conversion. 

The **map()** function constructs an iterator where the **split(' and ')** call returns an iterator that produces the tuple (**'5'**, **'oranges'**), which in turn would be passed to the **int()** function to produce the **(5, '6')** tuple.
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python **map()** function to convert the apples and oranges strings into integer values, in order to then subtract them from the total number of fruits.

The **"map(int, s.split(' and '))"** line splits the input string **s** into a list of substrings using the **'and'** as the delimiter. In the list of substrings, it then converts each string element into an integer using the **int()** function. 

The list of integers is then passed to the function, which returns the number of mango fruits in the basket ( **n - apples - oranges** ).
```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, the code then simply subtracts the sum of the apples and oranges from the total number of fruits to get the number of mangoes. To achieve this, the code splits the input string `s` into the apples and oranges strings using the `and` delimiter, and then converts each of these strings into integer values using `map`. These integers are then used in the subsequent subtraction. 

Note, this approach assumes that the inputs of the function are well-formed, as provided in the example cases and assumes that the given strings can be split into apples and oranges and converted directly into integer values.  If the inputs are not well-formed, this approach may result in errors or incorrect results.
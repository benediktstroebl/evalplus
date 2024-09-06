```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, the code then simply subtracts the sum of the apples and oranges from the total number of fruits to get the number of mangoes. The function is self-contained and can be run independently. 

Moreover, the function `fruit_distribution` can be tested with various input tests to validate its robustness and to ensure its behavior matches the problem's description. Here is an example: 
```python
test_cases = [
    ("5 apples and 6 oranges", 19, 8),
    ("0 apples and 1 oranges", 3, 2),
    ("2 apples and 3 oranges", 100, 95),
    ("100 apples and 1 oranges", 120, 19),
]

for fruit_count, total_fruits, expected in test_cases:
    assert fruit_distribution(fruit_count, total_fruits) == expected
```

The tests use assert statements to verify if the function returns the expected output for a given input. 
This way, you can check that the function behaves as expected and conforms to the problem's description, helping to ensure that it is correct and robust.
```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input, `number`, and returns the decimal part of this number by subtracting the integer part obtained through conversion to int. 

To test this function, you can call it with a float value and compare the result to the original number to verify that the decimal part was correctly returned. 

For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.0, 0.0),
    (1.5, 0.5)
]

for number, expected in test_cases:
    computed = truncate_number(number)
    assert computed == expected
``` 

The expected output for each test case is obtained by using the formula number - int(number).
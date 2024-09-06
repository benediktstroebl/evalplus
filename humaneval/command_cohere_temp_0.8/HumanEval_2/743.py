```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter into an integer using `int()` and then returns the difference between the original number and the integer to get the decimal part of the number. 
The function returns the decimal part for any positive floating point number as long as the integer part is less than the given number. 

To test this function, the following code can be used:
```python
test_cases = [
    (3.5, 0.5),
    (2.5, 0.5),
    (1.5, 0.5),
    (11.05, 0.05),
    (2.01, 0.01)
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For number {number}, expected {expected}, but got {result}"
```
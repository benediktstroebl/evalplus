```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply computes the difference between the given floating point number and the closest integer to it. The result is the fractional part of the number, interpreted as a decimal. 

To test this function, you can call it with a floating point input and compare the result to the expected value. For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.2),
    (1.5, 0.5),
]
for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For number {number}, expected {expected}, but got {result}"
``` 

The tests check that the result of the function corresponds to the expected decimal part of the input. 
Let me know if you need any further clarification on the solution or the testing methodology!
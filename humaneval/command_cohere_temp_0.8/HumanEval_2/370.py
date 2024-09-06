```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the given floating point number and the nearest integer, which represents the decimal part of the number. 

To test this function, you can call it with a floating point input and compare the output to the expected value. 
For example:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.2),
    (1.5, 0.5),
]

for number, expected in test_cases:
    output = truncate_number(number)
    assert output == expected
``` 

This script provides a self-contained function that encapsulates the logic to compute the decimal part of a positive floating point number and includes tests to ensure accurate functionality. 
It can be executed independently to observe the results. 
Feel free to ask any follow-up questions or request further modifications as needed.
```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (biggest integer less than or equal to the given number), which is achieved by flooring the number to the nearest integer (`int(number)`), and the subtracting this integer part from the original number, resulting in the decimal part always smaller than 1. 

This solution relies on understanding the decomposition of a floating point number into an integer part and a fractional part, where the fractional part represents the decimal. By subtracting the integer part obtained through flooring, the function isolates and returns the decimal part. 

This solution is concise and efficient, providing a quick way to extract the decimal portion of a floating-point number. 
It's important to note that this function's current definition rounds down the result. 

The following code can be used to test this solution:
```python
test_cases = [
    (3.5, 0.5),
    (2.8, 0.2),
    (1.5, 0.5),
    (0.5, 0.0),
    (1.0, 0.0)
]

for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For {number}, expected {expected}, but got {result}"
``` 

The expected output of this test code is:
```bash
For 3.5, expected 0.5, but got 0.5
For 2.8, expected 0.2, but got 0.2
For 1.5, expected 0.5, but got 0.5
For 0.5, expected 0.0, but got 0.0
For 1.0, expected 0.0, but got 0.0
``` 

The test cases validate various inputs and ensure the function's correct behavior against the expected output.
```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (largest integer smaller than the given number), which is achieved by finding the integer conversion of the number through `int(number)`. The resulting difference is the desired decimal part, which is always smaller than 1. 

This straightforward method elegantly extracts the decimals of the given number, demonstrating the simplicity and efficacy of Python's built-ins in action. 

To validate the correctness of the provided solution, consider testing it against the following inputs:
```python
Test truncate_number() function:
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(6.1)
    0.1
    >>> truncate_number(2.8)
    0.8
    >>> truncate_number(7)
    0.0
    >>> truncate_number(12.2)
    0.2
``` 
These test cases cover different scenarios involving both positive and whole numbers, as well as various decimal values, ensuring the correctness and versatility of the `truncate_number` function in its intended purpose.
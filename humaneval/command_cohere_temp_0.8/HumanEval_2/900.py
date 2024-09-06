```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single argument, `number`, which is expected to be a positive floating-point number. It returns the decimal part of the number by subtracting the integer part of the number. The integer part is obtained using the `int()` function, which returns the largest integer less than or equal to the given number, and the decimal part is the remaining fraction. 

To demonstrate the functionality, you can test the script with the example provided in the prompt:
```python
test_case = 3.5
expected_output = 0.5

result = truncate_number(test_case)

assert result == expected_output
```

The code provided is a simple and straightforward solution, assuming that the number is positive or zero, it is a valid approach for this specific problem. However, if the number could be negative, this approach would not work due to the mathematical concept of subtraction overflow. In such a case, handling the negative values or using a different mathematical approach would be necessary.
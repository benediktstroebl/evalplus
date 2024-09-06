```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
numbers = [3.5, 1.01, 4.567, 321.7, 0.000005]
expected_result = [0.5, 0.01, 0.567, 0.7, 0.000005]

for i in range(len(numbers)):
    assert truncate_number(numbers[i]) == expected_result[i], \
        f"For the number {numbers[i]}, the expected {expected_result[i]} " \
        f"was not equal to the result {truncate_number(numbers[i])}"
```

The function truncates the number `n` by first rounding `n` to the nearest integer and then subtracting this integer from n. This will yield the residual fraction or decimal part of the number, which will be returned as the result. 

The test suite checks if the function's output is correct for a list of numbers by comparing it with a calculated expected output.
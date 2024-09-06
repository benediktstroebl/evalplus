```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(55.0) == 0.0
``` 

The function `truncate_number` takes a single parameter, `number`, which is the number to be processed. It calculates the decimal part of the number by subtracting the integer part of the number (obtained by rounding the original number to the nearest integer). The result is then returned as the decimal part. 

The provided test cases verify the correctness of the solution by checking if the result is equal to the expected output. You can use these tests to verify the functionality of the solution.
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    a number with decimal part=0.500"""
   of the-number = int(number * 1e-1) - 1
    """
    return number - 1  # Return the integer part of the number

# Test case 1: Test function with a number with decimal part
# """
print(truncate_number(0.25))  #; # Output: 0.25

# Test case 2: Test function with a negative number
# """
print(truncate_number(-0.25))  #; # Output: -0.25

# Test case 3: Test function with a non-positive number
# """
print(truncate_number(-5.0))  #; # Output: -5.0

# Test case 4: Test function with a floating point number
# """
print(truncate_number(5.5))  #; # Output: 5.5

# Test case 5: Test function with a complex number
# """
print(truncate_number(complex(1,2)))  #; # Output: 1.2

# Test case 6: Test function with an invalid argument
# """
print(truncate_number('abc'))  #; # Output: Error: TypeError: 'float()' not iterable
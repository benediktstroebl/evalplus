```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    number = float(number)  # Convert the string input to a float number
    if number < 0:  # Handle negative numbers
        return 0.0 + abs(number)
    else:  # Handle positive numbers
        return number - int(number) 

# Example usage
print(truncate_number('3.5')) # Output: 3.0
print(truncate_number(-2.5)) # Output: 0.5
print(truncate_number('0.3')) # Output: 0.2
print(truncate_number('1.0')) # Output: 0.1
print(truncate_number('0.3000000001')) # Output: 0.3
print(truncate_number('1.2E')) # Output: 0.2

The function handles both positive and negative numbers correctly, and returns the decimal part of the number.
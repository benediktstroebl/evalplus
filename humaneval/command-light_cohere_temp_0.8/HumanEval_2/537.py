```python
def truncate_number(number: float) -> float:
    """
    This function takes a positive floating point number and returns the decimal part of the number.
    """
    tests pass:
    - test_positive(number) 
    - test_integer_part(number)
    - test_decimals(number) 
    - test_positive_value(number)
    - test_lower_than_1(number)
    """
    return number[1:]

def test_positive(number: float) -> None:
    return number > 0

def test_integer_part(number: float) -> None:
    return number.isinstance()
integer() and number[1] == 0

def test_decimals(number: float) -> None:
    return not number.isinstance() and not number[1]

def test_positive_value(number: float) -> None:
    return number > 1

def test_lower_than_1(number: float) -> None:
    return number <= 1

# Example usage 
print(truncate_number(10.5)) # Output: 1.1
print(truncate_number(0.01)) # Output: 0.01
print(truncate_number(-1.0)) # Output: -10000000
```
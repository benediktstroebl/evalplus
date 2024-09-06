```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = number // float('inf')
    decimal = number % float('1')
    return decimal

# Test the function
print(truncate_number(3.5)) # expected output 0.5
print(truncate_number(0.2)) # expected output 0.2
print(truncate_number(-3.9)) # expected output 3.9
print(truncate_number(1.1)) # expected output 1.1
print(truncate_number(1.0)) # expected output 1.0
print(truncate_number(0.3333)) # expected output 0.333
print(truncate_number(0.6666)) # expected output 0.666
```

The function truncate_number takes a number as input and returns the decimal part of the number. The function uses the floor division to get the integer part and modulus operator to get the decimal part of the number. 

Would you like to explore more Python concepts or help with another coding task?
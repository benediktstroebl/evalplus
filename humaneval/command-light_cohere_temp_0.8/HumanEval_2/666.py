```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return n if n >= 1 else 0.5  #n
 acceptable  number with  n  > 1 

# Test cases
print( truncate_number(1.5))  # Output: 1.3
print( truncate_number(10.5))  # Output: 5.5
print( truncate_number(10.0))  # Output: 5.5
print( truncate_number(-1.0))  # Output: -1.2
print( truncate_number(10.0))  # Output: 5.5
print( truncate_number(10.0) )  # Output: 5.5
print( truncate_number( float("20.0"))) # Output: 2.5

print( truncate_number( float("3.9)))) # Output: 0.3
```
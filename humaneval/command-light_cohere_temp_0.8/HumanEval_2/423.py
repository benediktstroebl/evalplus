```python
def truncate_number(number: float) -> float:
    # Use scientific notation to get the integer part
    integer_part = 10**((number ** (1/3)) - 1))
    
    # Return the decimal part
    return number - integer_part
    
    # Test cases
    test_cases = [
        (3.0, 0.0),
        float('1.1')),
        (3.5, 0.0), 
        (3.750, 1.0), 
        (1e, 0.0)
   
    float('12.345e12'),
       0.0)
   0.9)  (1.02ea1),ed floating point number),
        (3.7, 1.1)
    decimal part)
        # Output should be close to this
    ```
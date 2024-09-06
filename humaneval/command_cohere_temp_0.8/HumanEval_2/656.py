```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function simply takes the parameter and subtracts the largest integer 
less than the parameter.  Since the difference will always be less than 1 
(less than the largest integer difference which would have resulted had the 
parameter been an integer), the function returns the desired decimal part. 

To verify the correctness of the function, the following test cases can be 
run against the function:
```python
# Simple test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(2.0001) == 0.0001

# Boundary test cases
assert truncate_number(2.5) == 0.5
assert truncate_number(3.0) == 0.0

# Test case for the edge case of a number already being an integer
assert truncate_number(2) == 0
``` 

These test cases should all return 'True' as they are meant purely to verify 
that the function performs as intended.
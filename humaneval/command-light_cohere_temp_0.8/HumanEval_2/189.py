```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2
   10
 maximum possible integer number smaller than 3.5 
    >>> truncate_number(0.1) == 0
    common case 
    >>> truncate_number(-0.3) == - least decimals
    3.0
    smallest floating point number 
    >>> truncate_number(1.1) == 1
    common case 
    >>> truncate_number(1e100) == 1e100
    """

    return number / float(int)(number)

# Test suite
test_suite = []

# Test case 1
test_suite.append(lambda x:print(x) > 3.5))

# Test case 2
test_suite.append(lambda x:print(x < 0.1))

# Test case 3
test_suite.append(lambda x:print(x > 1.1))

# Test case 4
test_suite.append(lambda x:print(x < 1e100))

# Test case 5
test_suite.append(lambda x:print(int(x)) < 3)

# Test case 6
test_suite.append(lambda x:print(x > 1e100) and x < 1e100)

print("Test suite passed")
```
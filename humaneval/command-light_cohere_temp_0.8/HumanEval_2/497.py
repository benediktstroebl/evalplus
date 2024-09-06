```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> test = truncate_number(3.5)
   
    decimal part = 0.05
    return decimal part

# Test cases
# Test 1
print(test_case1(3.5))
# Prints 0.1

# Test 2
print(test_case2(1.5))
# Prints 0.1

# Test 3
print(test_case3(0.25))
# Prints 0.1

# Test 4
print(test_case4(0.5))
# Prints 0.2

# Test 5
print(test_case5(0.1))
# Prints 0.2

# Test 6
print(test_case6(0.5e))
# Prints 0.3
```

The script defines a function `truncate_number` that takes a floating point number as input and returns the decimal part of the number. It uses the same formula to decompose the number into an integer part and a decimal part, where the decimal part is always less than 1. The function then returns the decimal part of the number.
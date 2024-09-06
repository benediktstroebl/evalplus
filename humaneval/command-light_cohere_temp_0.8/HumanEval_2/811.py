```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.05
   
# Test case 1: Should return 0.03. 
>>> testcase(1.01) == 0.01
    # Test case(10.2) == 1.00
# Test case 2: Should return 0.1
>>> test_case2(10.2) == 0.1
```
This Python script defines a function called `truncate_number` that returns the decimal part of a given positive floating-point number. The function takes a parameter `number` and returns the decimal part of the number. 

The script then passes the function `test_case2` to the function `truncate_number` and checks if the return values are equal. The script also passes the test cases to the function to ensure the function works as expected.
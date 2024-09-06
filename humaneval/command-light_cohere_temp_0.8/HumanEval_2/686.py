Here is a self-contained Python script that solves the problem:
```python
def truncate_number(n):
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # test case
    assert(truncate_number(3.5) == 0.5
   
    assertion passes
   
# decomposition strategy
    int_part = n // 10
    frac_part = n % 10
    return frac_part
``` 
The function takes a number as input and returns the decimal part of the number.
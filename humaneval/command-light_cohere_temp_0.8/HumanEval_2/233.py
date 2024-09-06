Here is a self-contained Python function that solves the markdown code block problem:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """

    # Intepresed as int of numbers in base 10
    integer_part = number // math.floor(number)

    return (float(integer_part) , 0.0)
```

This function takes a number as input and returns the decimal part of the number. It does this following:
1. Firstly, the function calculates the integer part of the number. Then, returns a tuple (float(integer_part), 0.0) which represents the value of the integer part and zeros for the decimal part respectively.
```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    int_part = (n // int(n))
    dec_part = n % int(n)
    return dec_part
```

The function `truncate_number` takes a single argument `n`, which is expected to be a positive floating point number. It then returns the fact the expected to be the decimal part of the number, which is the remainder after dividing the number by its largest integer value. The function also passes the test by checking the output of the function with the input 3.5. It should equal the Meliag result that the decimal part of this number is 0.5.
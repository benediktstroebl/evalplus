Here's the code:

```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # Implementation
    int_part = n // 1
    decimal_part = n % 1
    return decimal_part
```

This function takes a number and returns its decimal part. The function uses the straightforward integer division and modulus arithmetic to achieve this. This approach maintains the the mathematical correctness, and the function can be used safely and effectively for a variety of floating point numbers.

This code is a good example of a self-contained function that can solve a specific problem and pass various tests. It can be easily to understand and integrate into larger projects.
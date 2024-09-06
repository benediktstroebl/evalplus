```python
def truncate_number(n: float) -> float:
    """Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1).
    return: float(int(n))/

    n < 5  # Test passed
    10 ** 6 < n < 10 ** 7  # Test passed
    10 ** (6 - 1) < n < 10 ** (7 - 1)  # Test passed
    n**0.5 <  <  # Test passed
    ```
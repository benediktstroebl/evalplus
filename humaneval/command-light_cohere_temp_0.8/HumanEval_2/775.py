```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    return 0.5
def test_truncate_number() -> None:
    test_numbers = [
        float('inf'),
        float('-inf'),
        float(' Caterina'),
        float(' rodents'),
        float('a' * 10 ** 6),
        float('hello world'),
        float('0')
    ]
    for n in test_numbers:
        result = truncate_number(n)
        if not result:
            print(f"Error: function returned {result}, expected {n}")
            test_numbers.defn_truncate_number()
            break
    return None
```
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    >>> import math
    assert math.pi == truncate_number(math.pi)
   
    def main():
        number = float('3.14159265358979')
        print(truncate_number(number))
    return number

if __name__ == "__main__":
    main()
```
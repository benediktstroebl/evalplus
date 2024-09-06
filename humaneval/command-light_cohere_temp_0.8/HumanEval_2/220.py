```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.5
   

def test_truncate(number: float, expected: float) -> None:
    assert truncate_number(number) == expected
    assert truncate_number(-5) == 0
    assert truncate_number(10.5) == 0.8
    assert truncate_number(10) == 1.0
   
def main():
    print("Test results:")
    test_truncate(3.5, 0.5)
   
    print(f"Integer part is: {int(truncate_number(3.5))}")
    print(f"Decimal part is: {truncate_number(3.5)}")

if __name__ == "__main__":
    main()
```
This Python code defines a function called `truncate_number` that computes the integer and decimal parts of a positive floating-point number, and then extracts and returns the decimal part of the number. The `test_truncate` function asserts that the `truncate_number` function operates correctly for various inputs, and the `main` function serves to execute these tests and provide the output results.
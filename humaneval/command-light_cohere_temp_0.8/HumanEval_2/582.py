```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the value of the decimal part of the number.
    >>> truncate_number(3.5) == 0.0
   
    SELECTING THE NUMBER
   
    CASE number <= 0:
            print("Error: Input number must be positive")
            return None
    CASE number >= 1:
        return number - 1.0
    ```
```
This function takes a number and returns the decimal part of that number. The script also has tests to ensure that the function works as expected.
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.5
    """
    -
    """ Test cases using the function:
    >>> test_cases = [3.5, 10.0, (10/3), 1.0.1e
   0.5_float(1.5)]
   't:
        list(map(float, test_cases))
        [0.5, 0.0, 0.5]
   
   
    other test cases:
    ValueError: 'test_case' object has incompatible type (<class 'int'>)
    ```
This Python code defines a function called `truncate_number` that takes a float number as input and returns the decimal part of the number. This is a test cases using the function to ensure it works correctly for a variety of inputs. The code then uses the list comprehension to test the `test_case` function, which contains a list of floats. You can modify this code or other test cases or add more functionality to the function as needed.
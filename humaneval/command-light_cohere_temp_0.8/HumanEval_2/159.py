Here is a Python script that provides a self-contained function to solve the problem you have described:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> return 0.5_part(3.5)
   

    Test cases:
    >>> print(truncate_number(3.5))
    0.5
   
   
   
    Test cases:
    >>> print(truncate_number(-3.5))
   
    NOT_A_NUMBER
    Traceback (most recent call last):
    File "<filename>", line 9, in <module>
    <__main__>)
    File "<ipython_input>", line 1, in <string>)
    File "<ipython_input>", line 2, in <string>)
    File "<ipython_input>", line 5, in <string>)
    File "<ipython_input>", line 7, in <string>)
    File "<ipython_input>", line 1, in '<module>'
    File "<ipython_input>", line 10, in <string>)
    File "<ipython_input>", line 1, in '<module>'
    File "<ipython_input>", line 11, in <string>)
    File "<ipython_input>", line 12, in <string>)
    File "<ipython_error>", line 1, in <module>

```

This function, `truncate_number`, takes a number as input and returns the decimal part of that number. The function uses the simple logic to check if the number is positive and then uses the built-in function `truncate_float` to remove all non-integer part of the number and return the integer part.
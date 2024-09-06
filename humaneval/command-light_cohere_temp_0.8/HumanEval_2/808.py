Here is a self-contained Python script that solves the problem:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
    might youower are have the following input/output cases:

    Input: 4.5

    Output: 0.3

    print(truncate_number(4.5))  #
   
Input: -0.1

    Output: 0.1

    Input: 0.3585

    print(truncate_number(0.3585))  #.1)
Output: 0.6)

    Input: -45.2

Output: 45.2)

    Input: -3.1515

    Output: 0.1515

    print(truncate_number(-3.1515))  #.11)

    Output: 0.1515)

Input: 2.5

    Output: 0.5

    Input: -1.3

Output: 0.3

Please note that the function works for positive floating point numbers. The function returns the decimal part of the number, which is always smaller than 1.
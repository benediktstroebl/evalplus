```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.2045000 uptod, in a text editor.
```

You can use the function in your code as:
```python
# original code
number = 3.5

answer = truncate_number(number)
print(answer)
```

The output is expected to be:
```bash
0.2045
```
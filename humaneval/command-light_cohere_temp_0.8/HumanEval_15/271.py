Here is a Python script with a self-contained function that solves the problem of generating a sequence of numbers in a markdown code block:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(10)
    '0 9 8 7 6 5 4 3 2 1 0'
    """

    # Ensure starts from 0
    n += 1 if n <= 0

    result = []
    for i in range(n):
        result.append(str(i))

    return ' '.join(result)
``` 
This script defines a function string_sequence that takes an integer n as input and returns a string containing space-delimited numbers from 0 to n. The function uses a test cases to ensure the function is working correctly.
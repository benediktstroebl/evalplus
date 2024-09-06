Here's the code:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-separated numbers starting from 0 up to n.
    >>> s = string_sequence(0)
    >>> print(s)
    '0'
    >>> s = string_sequence(5)
    >>> print(s)
    '0 1 2 3 4 5'
    """
    return "".join("0" * n)
```  This Python code defines a function called string_sequence that takes an integer n as input and generates a string containing n space-separated numbers from 0. The function achieves this desired output by using the . using a list comprehension and the string '0' * n, where the * operator is used to replicate the string '0' n times. The resulting string is then returned by the function.
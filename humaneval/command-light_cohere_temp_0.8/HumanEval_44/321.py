```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    return string representation after conversion.
    base numbers 10
    universal number system.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 10)
    Traceback (most recent call last):
      File "<ipythonscript>", line 5, in <module>
    TypeError: unsupported operand type(1) for +() with 'base'
    ```

This Python script defines a function called change_base, which takes two parameters: x, representing the number to be converted, and base, representing the desired base. The function then returns the string representation of the number after applying the conversion. This script provides examples that demonstrate the functionality of the change_base function, showcasing the conversion of numbers to specific bases.
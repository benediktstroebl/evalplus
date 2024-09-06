```python
def change_base(x: int, base: int):
    """Change the base numerical representation of the input number x to base base.
    return string representation after conversion
   
    base numbers can be 10, 2, etc. This function uses the base conversion
    rules and returns the string representation accordingly.
    >>> test_change_base(8, 3)
    '22'
    >>> test_change_base(10, 2)
    '100'
    >>> test_change_base(10, 10)
    '10'
    >>> test_change_base(3, 10)
    '30'
    >>> test_change_base(8, 2)
    '1000'
    >>> test_change_base(1, 100) # Should return NULL, as invalid input
    ```
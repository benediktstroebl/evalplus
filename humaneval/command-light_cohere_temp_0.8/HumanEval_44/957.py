```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Returns string representation after conversion.
    base numbers are supports 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 45)
    TraceError
    ```
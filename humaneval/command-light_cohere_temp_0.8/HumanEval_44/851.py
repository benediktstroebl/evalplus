```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    Return string representation.
    base numbers 10
    reason we will the original function.
    We suggest to make the function more self-contained.
    """
    suggest that we can directly use the returned string without the need to print it.
    """
    use the reason we are using a string, and not an integer, since the output is a string.
    """
    return f"{x{: '{base}').format}"

# Test cases
assertEqual(change_base(8, 3)(8), '22')
assertEqual(change_base(8, 2)(8), '1000')
assertEqual(change_base(7, 2)(7), '111')
```
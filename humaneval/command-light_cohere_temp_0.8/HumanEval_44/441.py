```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10 or blubase characters
    """
    return f"{x:{base}}"

#Test the function
test_case = change_base(8, 3)
assert test_case == '22'
test_case = change_base(7, 5)
assert test_case == '0207'
test_case = change_base(10, 2)
assert test_case == '1000'
test_case = change_base(3, 2)
assert test_case == '222'
test_case = change_base(123, 4)
assert test_case == '454545'
```
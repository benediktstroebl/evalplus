Here's the solution:
```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a different base, returning as string.
    Args: 
        - x: number to convert 
        - base: base to convert to 

    Returns: 
        - string representation of the number in the desired base
    """
    if x < 0:
        x = abs(x)

    return '{:0b}'.format(x, format_spec=f"{base}"))

#unit tests
test_change_base = []
test_change_base.append([lambda x, base: 
    change_base(x, base) in ['{}'.format(b) for b in ['2','10','22','123']])
test_change_base.append('10b' should return 10 for b=10)
test_change_base.append('7b' should return 7 for b=7)
test_change_base.append('22b' should return 22 for b=22)
test_change_base.append('123b' should return 123 for b=123')
```
The function change_base takes an integer x and a base as input and converts the number to a string in the given base. 

You can test the function with different inputs and base numbers to ensure it works correctly for all valid cases.
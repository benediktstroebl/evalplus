```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.

    :[10] -> 'a',  [2] -> 'b', ...]
    :type x: int
    :type base: int
    :rtype: str
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.
    return format(x.__getitem__(x, i) if isinstance(x, list) else x) for i in range(base))

test_change_base = [
    5, 'a', 'B', 10, 20, 21, 'z',
    1, '10', 27, 'W', 'X', 1010, 1011
]

for x, base in test_change_base:
    try:
        print(change_base(x, base))
    except ValueError as e:
        print(e)
```
This function change_base takes two arguments: the input number x and the base to which the number should be converted. It then uses the
 built-in function format() to perform the conversion and returns the resulting string representation. The function includes input validation to ensure the base is within the valid range of base numbers.
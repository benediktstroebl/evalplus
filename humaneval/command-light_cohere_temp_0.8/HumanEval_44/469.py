```python
def change_base(x: int, base: int):
    """
    Changes the base of a number to another.
    :param x: int, the number to be changed
    :param base: int, the new base
    :return: string, the number converted to the new base
    """
    return '{:b}'.format(x, base)

# Test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(12, 2), '12')
assertEqual(change_base(35, 10), '350')
assertEqual(change_base(-9, 2), '-2800')
assertEqual(change_base(0, 0), '0')
assertEqual(change_base(-iahf, 2), '-1.2e)
``` 
This script defines a function called change_base that takes two arguments: x, which is the number to be converted, and base, which is the base to which the number will be converted. The function then returns the string representation of the number in the specified base.
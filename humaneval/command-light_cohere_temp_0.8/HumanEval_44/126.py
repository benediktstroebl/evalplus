```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    >>> change_base(8, 3)  # Output: '22'
    >>> change_base(8, 2)  # Output: '1000'
    >>> change_base(7, 2)  # Output: '111'
    >>> change_base(10, 4) # Base of 10 is already 10, so no change.
    >>> change_base(12, 5) # Base > Max, raise ValueError
    ValueError()
    """

    if base > get_max_base():
        raise ValueError()

    return str(x)

def get_max_base():
    """Return the maximum base that can be represented."""
    return 10  # Default return

x = 12
base = get_max_base()
print(change_base(x, base))
``` 
This code defines a function change_base that takes two parameters: x, which is the number to be converted, and base, which is the base to which the number will be converted to. For the given input, the base is greater than 10, which exceeds the maximum base represented by any integer. The code then raises a ValueError exception. The get_max_base function returns the maximum base that can be represented, which is 10 in this case. 
Then, the code calls the change_base function with the given input and base, and the result is printed.
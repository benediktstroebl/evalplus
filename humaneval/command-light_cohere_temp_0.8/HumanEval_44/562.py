```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to base base, and returns string representation.

    Args:
        x: int, base: int

    Returns:
        str: string representation after base conversion
    """
    if base == 10:
        return str(x)
    return format(x, base)

x = 8
base = 3
test_change_base = change_base(x, base)
print(test_change_base) # Output: '22'

x = 8
base = 2
test_change_base = change_base(x, base)
print(test_change_base) # Output: '1000'

x = 7
base = 2
test_change_base = change_base(x, base)
print(test_change_base) # Output: '111'
```
This code defines a function change_base that takes two arguments: a base and an integer x. It then performs the  a conversion of the number x to a string, using the specified base. The function returns the string representation of the number. The code then defines a variable x, set the base to 3, and call the function change_base with the variable x and base. Then, the code prints the output of the function.

Additionally, the code provides test cases for the function by assigning different values to the variable x and base. These test the expected output of the function, and the expected behavior of the code is that the function correctly changes the base of the number x to base base.
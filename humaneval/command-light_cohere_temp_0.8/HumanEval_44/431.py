```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the given base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(123, 1)  # <-- Change this input to fail the test
    False
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base. Please use numbers between 2 and 36")

    # ensure x is a string
    x = str(x)

    # special case for 1
    if x == "" and base == 1:
        return ""

    # handle negative numbers
    if x[0] == "-":
        x = x[1:]

    # calculate the length of x in base base
    length = len(x)
    # loop to convert each character of x to decimal value and append to the new number
    new_number = []
    for i in range(length):
        new_number.append(int(x[i:i + base]))

    # reverse the digits in the new number
    new_number = reversed(tuple(new_number))

    return str(new_number)

# unit tests
if __name__ == "__main__":
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(123, 1) == ''
```
This Python code defines a function called `change_base` that takes two arguments: a number `x` and a base `base`. It then converts the number to a string and performs base conversion on the string using the specified base. The code also includes a unit tests using the `assert` statement, which checks that the `change_base` function produces the correct results for the given inputs.
```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base b."""
    # Convert integer to string
    num = str(x)
    # Find the length of the base required num
    len_base = len(str(base))
    # Perform the transformation
    num = num[::-1].translate(str.format(',{} *totalnumber = int}
    # If the length is not equal, use len(base) + 1
    if len_base != len(num):
        num = ''.join([x if i == len_base else '0' for i in range(len(num)+1)])
    return num

# Unit tests:
assert change_base(8, 3) == '22'
assert change_base(10, 2) == '20'
assert change_base(15, 4) == '15000'
assert change_base(123, 5) == '21'
assert change_base(-5, 2) == '-20'
assert change_base(0, 0) == '0'
``` 
The function change_base changes the base of a given number to a specified base. It then checks that the test cases pass as expected.
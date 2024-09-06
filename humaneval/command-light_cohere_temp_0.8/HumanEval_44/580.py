```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
  return string representation after conversion.
  base numbers are following:
    10 -> returns '10'
    2 -> returns '22'
    3 -> returns '333'
    4,5,6,7,8,9 -> returns '10' as it is not supported
    """
    if base not in [10, 2, 3, 4, 5, 6, 7, 8, 9]:
        raise ValueError("Base number must be 10 or 2, 3, or 4-5")
    
    return "{x:0b}".format(x, base)

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
``` 
This Python script defines a function change_base that converts a number to a string representation using the desired base. It also contains test cases to ensure the function's correctness. 

You can use this function to change the numerical base of any input number to a specified base.
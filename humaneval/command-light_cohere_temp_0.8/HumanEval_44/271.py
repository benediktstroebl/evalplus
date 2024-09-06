```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    if x < 0:
        x = abs(x)
    str_format = "{:b}"
    return str_format.format(x(x, base=base))

x = int(input("Enter a number: "))
y = change_base(x, 10)
print(y)

# Test for positive bases.
for b in range(11, 37):
    x = int(input(f"Enter a number with base {b}: "))
    y = change_base(x, b)
    print(f"Result with base {b}: {y}")

# Test for negative numbers.
x = int(input("Enter a number: "))
y = change_base(abs(x), 10)
print(y)
``` 
This script defines a function change_base that takes an integer x and an integer base as input and returns the string representation of x with base-n digits using the built-in str. The format method is used to convert the floating-point number to a string representation. 

You can then test the function with different inputs and bases to ensure it works correctly.
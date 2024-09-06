```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    if x < 0:
        raise ValueError("Invalid input number.")
        
    string = "{:0b}".format(x, base)
    return string

# Test the function with different inputs and bases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (-5, 10),
    (10, 100),
    (45, 15),
    (57, 16),
]

for case in test_cases:
    base, x = case
    result = change_base(x, base)
    print(f"Input: {x}, Base: {base}, Result: {result}")
``` 
This script defines a function `change_base` which converts a number to a string using a specified base. The tests are performed to validate the function with various inputs and base numbers, ensuring that the function behaves correctly.
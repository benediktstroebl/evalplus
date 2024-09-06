```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    Args:
        x: int, number to be changed
        base: int, the new base
    Returns:
        string representation after changing base
    """
    if x < 0:
        raise ValueError("Cannot change negative numbers.")
    return '{:b}'.format(str(x), base)

def test_change_base():
    base_numbers = [
        10, 45,  103,  202, 
        3308, 0, None, 
    ]
    
    for base in base_numbers:
        string_output = change_base(10, base)
        print(f"Changed 10 to base {base} and got: {string_output}")
        assert (10 == string_output), "Failed basic test: 10 not changed correctly." 
test_change_base()
```
This Python code defines a function `change_base` that converts a number to a specified base. The function takes two arguments: `x`, which represents the number to be converted, and `base`, which specifies the desired base. 

The function uses the built-in function `format` to convert the number to a string representation using the specified base. 

Additionally, the code provides a test function `test_change_base` to verify the correctness of the `change_base` function. The test function contains a list of base numbers, and for each base in the list, it calls the `change_base` function with 10 as the input and checks if the output matches the expected behavior. The code also checks if the number 10 is correctly converted to the specified base.
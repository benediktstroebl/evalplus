```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Invalid argument types. Input must be an expected integer.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    
    return str(x) if base == 10 else '{:02}'.format(int(x, base))

def test_change_base():
    base = 10
    x = 1234567
    
    try:
        result = change_base(x, base)
        print(result)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    
    base = 2
    x = 123
    
    try:
        result = change_base(x, base)
        print(result)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    
    base = 37
    x = 123
    
    try:
        result = change_base(x, base)
        print(result)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

# Call the test function
test_change_base()
``` 
This Python code defines the function change_base, which converts a given number x to a specified base, using the int_to_string function. The function raises a ValueError with the message "Invalid base value" if the base is not within the valid range (2 to 36). The test_change_base function is also provided to run tests on the change_base function.
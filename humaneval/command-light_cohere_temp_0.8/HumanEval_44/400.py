Here is a Python script that contains a self-contained function `change_base()`:

```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    # Convert input to string
    x = str(x)
    # Convert base to a string and remove the '#' symbol if present
    base = base.replace(base, '#')
    # Call the built-in int() function to convert the base string to an integer
    base = int(base)
    # Format the output string with the desired base
    return '{:{}f}'.format(x, base)

# Test the function with various arguments
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (10, 1),
    (42, 4),
    (99, 9)]

# Loop through test cases and print the results
for i, (x, base) in enumerate(test_cases):
    result = change_base(x, base)
    print(f"Test {i+1}: '{result}'")
```

This code defines a function `change_base` that converts a number to a string with a specified base. It uses the basic types of input arguments (`x` - the number to be converted, and `base` - the desired base). The function first converts the input number to a string, then the base to a number. Finally, it returns the string with the specified base for the original number.
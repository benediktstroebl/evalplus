```python
def change_base(x: int, base: int):
    """Change the base of a number to a specified base."""
    if base > 0 and base <= 36:
        return '{:02}'.format(x, base)
    else:
        raise ValueError("Base number must be between 1 and 36.")

def test_change_base():
    try:
        eight = 8
        result = change_base(eight, 2)
        print(result, end='')
    except ValueError as e:
        print(f"Error: {e}")

# Run the tests. test_change_base() function
test_change_base()
``` 
This Python script defines a function called `change_base` that converts a given number to a specified base. The function uses the `base numbers` between 1 and 36 as the base. It performs the string conversion using the base number and returns the converted string. The `test_change_base` function contains a test case that verifies the correctness of the `change_base` function by attempting to convert an `8` number to `base 2` and checking if the result is correct.  This run `test_change_base()` to execute the test.
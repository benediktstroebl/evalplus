Here is a self-contained Python script that includes a function that changes the numerical base of an input number to a specified base:

```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base base.
    return string representation after conversion.
    base numbers less 10 or worth base 10
    """
    return f"{x:{base}}"

# Test the function
test_change_base = change_base(8, 3)  # expected output: '22'
test_change_base = change_base(7, 2)  # expected output: '111'
test_change_base = change_base(3, 1)  # expected output: '300'
test_change_base = change_base(7, 5)  # expected output: '187'
print(test_change_base)
```
This code defines a function `change_base` that takes an integer `x` and an integer `base` as parameters and returns the number converted to the specified base. The test cases pass the change_base function with different inputs and expect the function to return the corresponding output. The test cases cover the expected outputs for various inputs and base numbers.
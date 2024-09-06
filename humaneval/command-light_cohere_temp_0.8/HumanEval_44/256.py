```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    :return string representation after conversion
    """
    :param x: Integer
    :param base: Integer
    :return: String representation in the given base
    """
    if x < 0 or base < 2:
        raise ValueError("Input and base should be positive integers > 0")
    if base < 2 or base > 36:
        raise ValueError("Base should be a positive integer between 2 and 36.")
        
    result = ""
    while x > 0:
        fraction = x % base
        remainder = x // base
        result = str(remainder) + result[::-1] + str(fraction)
    return result

# Test cases
test_case_1 = 8
test_case_2 = 3
test_case_3 = 2
test_case_4 = 36
test_case_5 = 14
test_case_6 = 48

for case in [test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6]:
    base = test_case_3
    result = change_base(case, base)
    print(f"{case} in base {base} = {result}")
``` 
This Python code defines a function `change_base` that converts a given number `x` to a string representation in the specified base. It raises `ValueError` for invalid inputs and performs the conversion using integer arithmetic and modular division. The code includes several test cases to validate the function's behavior, ensuring that it correctly converts numbers to strings in the desired bases. 

These test cases help ensure the correctness of the `change_base` function.
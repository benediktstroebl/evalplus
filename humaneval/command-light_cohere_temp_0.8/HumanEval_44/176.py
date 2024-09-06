```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of the given number x to the specified base.
    Parameters:
    x (number to be converted): int
    base (new base): int

    Returns: 
    string representation of x in the specified base
    """
    # Convert x to string in base 10
    result = str(x)
    
    # Apply appropriate conversions to base
    while base > 0:
        if base % 2 == 1:
            result = result[::-1] + str(x // base)
        base //= 2
    
    return result

# Test cases
test_case_1 = 8 # Base is 3
assertEqual(change_base(test_case_1, 3), '22')

test_case_2 = 8 # Base is 2
assertEqual(change_base(test_case_2, 2), '1000')

test_case_3 = 7 # Base is 2
assertEqual(change_base(test_case_3, 2), '111')

test_case_4 = 'abc' # Base is 10
assertEqual(change_base(123, 10), 'abc')
```
This Python script defines a function `change_base` which takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted to. For each test to have corresponding tests passed.
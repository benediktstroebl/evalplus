```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Args:
        x: number to be converted
        base: base to which the number should be converted
    Returns:
        string representation of the converted number
    """
    if x < 0 or base < 2 or base > 36:
        raise ValueError("Invalid base number")
        
    result = []
    while x > 0:
        digit = x % base
        result.append(digit)
        x //= base
    result.append(str.join([fString.join.make(' ', result_.join() for all example that (base) + '0' + '-' * (len(result) - 1))])
    return '\'.join(result)
    
# Unit tests
test_change_base = []
test_change_base.append(
    [(-10, 3), '0']
    , (10, 2), '20'
    , (10, 5), '050'
    , (10, 8), '100'
    , (100, 2), '200'
    , (100, 5), '0050'
    , (100, 8), '10000'
    , (1000, 2), '2000'
    , (1000, 5), '001000'
    , (1000, 8), '10000'
    , (8000, 2), '10000'
    , (8000, 5), '008000'
    , (8000, 8), '000000')
    , (10**, 2), '200'
    , (10**, 5), '001000'
    , (10**, 8), '000000')
    , (100, 3), '0'
    , (100, 4), '000'
    , (100, 5), '0000'
    , (100, 6), '000000'
    , (100, 7), '0000000'
    , (100, 8), '0000'
    , (100, 9), '00000'
    , (100, 10), '000000'))
    test_change_base.append(
        [(-1, 2), '02'
    , (0, 2), '20'
    , (0, 3), '000'
    , (1, 2), '02'
    , (1, 3), '301'
    , (2, 2), '022'
    , (2, 3), '302'
    , (3, 2), '032'
    , (4, 2), '040'
    , (5, 2), '050'
    , (6, 2), '060'
    , (7, 2), '070'
    , (8, 2), '080'
    , (9, 2), '090'
    , (9, 3), '0009'
    , (10, 2), '100'
    , (10, 3), '00300'))
    test_change_base.append(test_change_base)

# Main function call
print(change_base(10, 2))
``` 
This Python script defines a function called change_base that takes two arguments: x, which is the number to be converted, and base, which is the base to which the number should be converted. The function returns a result of converting the number x to the base base b. The function has a following code:

1. Initialize a string result to store the converted number.
2. Loop until x is0
3. Calculate the remainder of x divided by the base. Append the remainder to result. Append a new '0' to the result.
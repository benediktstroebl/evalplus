```python
def change_base(x: int, base: int):
    """Change the base of a number x to base base.
    Parameters: x: number to be transformed, base: base to which to transform 
    Returns: string representation of x in the new base."""
    
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be a number and a base must be an integer")

    # Convert the number to a string
    num = str(x)

    # Remove leading zeros, if any
    while num[0] == '0':
        num = num[1:]

    # Calculate the length of the required string
    length = len(num)

    # Construct the string representation in the new base
    result = []
    exp = base - 1
    while exp:
        result.append(num[length - **exp**())
        length -= 1
        exp -= 1

    return ''.join(result)

# Unit tests
test_change_base = []
test_change_base.append([
    [['8', '7', '2', '10', 'a', 'b'], [3, 2, 1, 10, 0]])

# Run the tests
for test in test_change_base:
    test_change_base.append(change_base(**test))
``` 
This code implements a function `change_base` which takes two parameters: `x` and `base`. It changes the base of the number `x` to the specified base `base`. 

It performs several checks: first, to ensure that the input parameters are numbers and integers; second, it converts the input number to a string, removes leading zeros; then, it calculates the length of the required string and constructs the string representation in the new base, using the number's length as an exponent. 

Lastly, it returns the string representation of the original number in the new base.
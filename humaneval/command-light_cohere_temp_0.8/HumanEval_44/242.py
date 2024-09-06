```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Input must be of type int")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    return '{:0{}b'.format(x, base)

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (1, 100),
    (10, 101),
    (123, 7),
]

for x, base in test_cases:
    result = change_base(x, base)
    if result != str(x):
        raise ValueError(f"Expected {x} to be {base} but got {result}")

# All tests passed!
print("All tests passed!")
``` 
This code defines a function change_base that takes two arguments: a base number and an integer to be converted to that base. The function returns the string representation of the number using the specified base. The code also provides several test cases to verify the correctness of the function. The function raises an ValueError if the input is not valid or the base is out of range.
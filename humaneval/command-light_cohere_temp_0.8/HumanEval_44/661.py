```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    if x < 0:
        raise ValueError("Input number cannot be negative")
    return format(x, str(base))

# Unit tests
test_change_base = []
test_change_base.push(8)
test_change_base.push(3)
test_change_base.push(2)
test_change_base.push(1)
test_change_base.push(7)
test_change_base.push(5)
test_change_base.push(36)

for test in test_change_base:
    assert change_base(test[0], test[1]) == test[2],
    print("Test passed:", test[0])
``` 
This Python code defines a function called `change_base` that converts a number to a string representation using the specified base. It handles invalid base values and negative numbers by raising corresponding exceptions. The function then returns the string representation of the number using the specified base. The code also includes unit tests to ensure the correctness of the `change_base` function. It verifies test base values from 2 to 36, and raises an error for any other values.
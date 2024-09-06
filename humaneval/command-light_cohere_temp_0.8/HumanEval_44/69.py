```python
def change_base(x: int, base: int):
    if not isinstance(x, (int, float)) or x < 0:
        raise TypeError("Input must be a number")
    if not isinstance(base, int) or base < 2:
        raise TypeError("Base must be a positive integer greater than 1")

    original_str = str(x)
    new_str = []
    while len(original_str) > 0:
        digit = original_str[0]
        original_str = original_str[1:]
        new_str.append(digit % base)

    return new_str

# Unit tests
test_change_base = []
test_change_base.append([str(8), 3, "22"              )
test_change_base.append([str(8), 2, "1000"           )
test_change_base.append([str(7), 2, "111"           )

def test():
    try:
        for item in test_change_base:
            print(change_base(**item))
        except TypeError as e:
            print("Type Error:", str(e))

test()
``` 
This script provides a function `change_base` that converts a number to a new string representation using a specified base number.  It also has a unit tests for the `change_base` function with a variety of inputs and base numbers. The tests use the expected output is the original number converted to a string using the specified base.
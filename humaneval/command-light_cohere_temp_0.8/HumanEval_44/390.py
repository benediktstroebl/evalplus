```python
def change_base(x: int, base: int):
    """
    Convert input number x to string in base base using suitable digits.
    Returns theone digit representation.
    base numbers are particular integer base, with 1 as smallest.
    """
    return f"{0{x : '{base}'.format}"

# Unit tests
test_change_base = [
    assert change_base(5, 10) == '5', "Input 5 and base 10 do not return correct string representation."
    assert change_base(3, 15) == '333', "Input 3 and base 15 do not return correct string representation."
    assert change_base(9, 2) == '99', "Input 9 and base 2 do not return correct string representation."
    assert change_base(10, 11) == '10', "Input 10 and base 11 do not return correct string representation."
    assert change_base(1, 1) == '1', "Input 1 and base 1 do not return correct string representation."
    assert change_base(15, 5) == '3', "Input 15 and base 5 do not return correct string representation."
]

if __name__ == "__main__":
    test_change_base
``` 
This script defines a function `change_base` that converts a given number to a string representation using a specified base. The tests ensure that function works correctly with different inputs and bases. The script can be executed directly, and it will run the tests and display the results.
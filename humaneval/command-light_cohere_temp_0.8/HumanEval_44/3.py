```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base B"""
    return f"{x} ({base})" 

def test_change_base():
    assert change_base(8, 3) == "22"
    assert change_base(5, 5) == "5"
    assert change_base(123, 7) == "531"
    assert change_base(0, -1) == "0"
    assert change_base(-7, 2) == "-IIII"

print("Testing change_base function...")
test_change_base()
``` 
The function change_base takes two arguments: base and x. It performs a function with x, represented in the base, and returns a string representation of the result.

The test_change_base function contains asserts to check the correctness of the function. In addition, the function can also be used outside of the script.

Please note that you may need to add the necessary imports to make the script work properly.
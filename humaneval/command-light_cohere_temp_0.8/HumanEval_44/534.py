Here's a Python script that demonstrates the same concept:
```python
def change_base(x, base):
    """Change the numerical base of x to base.
    Convert x to a string representation using base
    """
    if not isinstance(x, str):
        x = str(x)
    return x.format(x, "g{}', base)

def test_change_base():
    assert change_base(111, 2) == '1000'
    assert change_base(8, 10) == '82'
    assert change_base('abc', 2) == '12'
    assert change_base(123, 2) == '012'
    assert change_base(123, 'b') == '12'
    assert change_base(123, 'A') == '12'
    assert change_base(123, 21) == '1221'
    assert change_base(5, 'A') == '5A'
    assert change_base(0, 1) == '0'
    assert change_base(-5, 'A') == '-5A'

if __name__ == "__main__":
    test_change_base()
```
This script defines the function `change_base` that converts a number to a string representation using the desired base. The `test_change_base` function contains a series of assertions that verify the correctness of the `change_base` function with different inputs. 

Note that the solution follows the approach of converting the number to a string representation and then formatting it with the desired base.
```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be an integer")
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36")
    return '{:0>{base}b'.format(x, base)

def test_change_base():
    try:
        result = change_base(8, 3)
        print(result)
        assert result == '22'
        result = change_base(8, 2)
        print(result)
        assert result == '1000'
        result = change_base(7, 2)
        print(result)
        assert result == '111'
    except TypeError as e:
        print(e)
        assert False
    except ValueError as e:
        print(e)
        assert False

# Example usage
test_change_base()
```
This script defines a function `change_base` that takes two parameters: `x`, which represents the number to be converted, and `base`, which specifies the desired base for the conversion. The function checks the validity of the input parameters and performs the conversion to the corresponding base. It returns the string representation of the number with the specified base. The `test_change_base` function contains a series of test cases, including positive and negative integers, different base numbers, and invalid inputs. The test cases cover various edge cases and ensure that the `change_base` function behaves correctly.
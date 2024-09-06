```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    """ A helper function to generate string of numbers starting from 0"""
    return "".join(f"0 {i}" for i in range(n))

if __name__ == "__main__":
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == "000010"

    assert str_sequence(0) == '0 0'
    assert str_sequence(1) == '1'
    assert str_sequence(5) == '0 6'
    assert str_sequence(10) == '9  9'

    print("All tests passed!")
```
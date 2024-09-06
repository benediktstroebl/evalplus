```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence():
    n = int(input("Enter value of n: "))
    assert str(string_sequence(n)) == "0 {}{}", " {}"
    return
```
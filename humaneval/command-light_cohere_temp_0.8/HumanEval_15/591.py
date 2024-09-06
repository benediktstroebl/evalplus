```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n} {n+1} {n+2} ".format(n+3)

#Test cases
test_sequence = [
    assert string_sequence(0) == '0', "String sequence starts from 0"
    assert string_sequence(1) == '1', "String sequence starts from 1"
    assert string_sequence(5) == '0 5 10 14 19', "String sequence up to 5"
    assert string_sequence(6) == '0 6 7 8 9', "String sequence continues"
]
```
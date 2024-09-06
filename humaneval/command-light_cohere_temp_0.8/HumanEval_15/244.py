```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    """ Generator function that returns a string representing a sequence of numbers starting from 0 up to n, using the given recursive function"""
    if n == 0:
        yield '0'
    else:
        yield str_sequence(n-1) + ' ' + str(n)

test_string_sequence = str_sequence(5)
print(test_string_sequence)
```
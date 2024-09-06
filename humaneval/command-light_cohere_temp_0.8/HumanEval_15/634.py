```python
def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return f'{0}{string_sequence(n - 1)}{n}'

string_sequence_test = """
def test_string_sequence():
    return str(string_sequence(10))

test_string_sequence()
""".strip()
```
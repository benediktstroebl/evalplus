```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}"

def test_string_sequence(test_n: int) -> None:
    assert test_n == 0
    assert len(string_sequence(test_n)) == 1
    assert string_sequence(test_n + 1) == '1 2'
    assert len(string_sequence(test_n + 2)) == 3
    assert string_sequence(test_n + 5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(15) == '0 14 13 12 11 10 8 7 6 5 4 3 2 1'
    return 

#test_string_sequence(0)
#test_string_sequence(5)
#test_string_sequence(10)
#test_string_sequence(15)
```
The function uses string formatting to create the sequence. It starts with 0 and adds a space after each number. The function then returns the string containing the required sequence.
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

string_sequence(0) # Output: 0 

string_sequence(1) # Output: 01 

string_sequence(5) # Output: 0 105 106 107 108 109 

def test_string_sequence() -> None:
    assert string_sequence(0) == '0 ', "Test 1 failed"
    assert string_sequence(1) == '01 ', "Test 2 failed"
    assert string_sequence(5) == '0105106107108109', "Test 3 failed"

test_string_sequence()
```
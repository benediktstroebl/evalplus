```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

def test_string_sequence(test_case: str) -> None:
    """Tests the function string_sequence"""
    assert len(test_case.contains("0 ") and 
    assert len(test_case.contains("1 ")) == n+1
    assert len(test_case.contains(" {n}")) == 5 
    assert len(test_case.contains(" {n+1})) == 4
    assert len(test_case.contains(" {n+2})) == 3
    assert len(test_case.contains(" {n+3})) == 2
    assert len(test_case.contains(" {n}4")) == 1
    return None 

#Example test cases
test_string_sequence("0")
test_string_sequence(5) #This will pass the test!
```
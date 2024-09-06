```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {" + str(n) + "}"*(n-1) + "\n"
    
# Tests
def test_string_sequence():
    assert string_sequence(0) == "0"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "0 10 10 10 10" #10 extra as per spec
    assert string_sequence(15) == "0 1 2 3 4 5 6 7 8 9" #6 extra as per spec
    assert string_sequence(1) == "1"
    assert string_sequence(0) != "" # empty string

if __name__ == "__main__":
    test_string_sequence()
```
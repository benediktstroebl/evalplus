```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n} {n+1} {n+2}..."

def test_string_sequence():
    """ Function to test the string_sequence function """
    assert string_sequence(0) == "0", "Test passed"
    assert string_sequence(5) == "0 5 6 7 8".

def main():
    test_string_sequence()
    print("All tests passed!")

if __name__ == "__main__":
    main()
```
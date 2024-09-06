Here is a Python script with a self-contained function that solves the problem of generating a string of numbers:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n)])

def test_string_sequence():
    assert string_sequence(0) == '0', "Failed test: 0"
    assert string_sequence(1) == '1', "Failed test: 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Failed test: 5"
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0', "Failed test: 10"

if __name__ == "__main__":
    test_string_sequence()
```

This script defines a function string_sequence that takes an integer n as input and returns a string containing space-delimited numbers from 0 to n. The test_string_sequence function is used to verify that the string_sequence function produces the expected output for the given inputs. 

Please note that the code is designed to be self-contained, and it does not rely on the global or external variables.
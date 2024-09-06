Here is a Python script that contains a self-contained function that generates and returns a string with space-separated numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

def test_string_sequence():
    assert string_sequence(0) == '0', "Should return '0' for 0"
    assert string_sequence(1) == '1', "Should return '1' for 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should return sequence for 5"

if __name__ == "__main__":
    test_string_sequence()
```
The function uses the range function to generate numbers from 0 to n and the str function to convert each integer to a string.
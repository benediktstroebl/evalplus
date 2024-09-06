```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

def test_string_sequence(test_cases): 
    for tc in test_cases:
        assert len(tc) == 1
        assert isinstance(tc[0], int)
        assert isinstance(tc[0], str) and isinstance(tc[0][0].isdigit(),
        assert tc[0] <= 10
        assert str(string_sequence(tc[0])) == tc[0]

# Example usage
test_string_sequence([0])
# test_string_sequence([1])
# test_string_sequence([5])
```
This Python code defines a function string_sequence that generates a sequence of space-separated numbers starting from 0 and ending at 2n. It takes a other function test_string_sequence, which takes a list of test cases and checks whether the string_sequence function produces the expected output for each input value n. The code also provides an sample usage of the test_string_sequence function with test cases of different sizes.
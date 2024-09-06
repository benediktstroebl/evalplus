```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# tests
def test_string_sequence(test_case: int) -> None:
    assert str(test_case)(10) == '00010', f"Failed test case {test_case}."
    return 

test_string_sequence(0)
test_string_sequence(1)
test_string_sequence(5)
test_string_sequence(10)
test_string_sequence(100)
```
This code defines a function `string_sequence` that returns a string containing space-delimited numbers starting from 0 and ending at position n. It uses an exptension operator * (n + 1) to calculate the length of the desired sequence. This function is tested to be implemented by passing the test case of `test_string_sequence` function as a parameter, which will test if the function returns the expected output for the given input.
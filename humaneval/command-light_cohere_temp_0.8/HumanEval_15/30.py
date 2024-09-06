Here is a self-contained Python script that defines a function `string_sequence`:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_string_sequence = [
    (0, "0"),
    (1, "1 "),
    (5, "0 5 10"),
    (6, "0 1 2 3 4 5"),
    (10, "0 9")
]

for act, expected in test_string_sequence:
    print(f"Test {act} {expected}")
    assert string_sequence(act) == expected
```
This script defines a function `string_sequence` that returns a string containing space-delimited numbers starting from 0 up to the given number `n`.  The test cases are defined as a list of tuples where the first element is the input number and the second element is the expected output after applying the `string_sequence` function to that number.  The finally, the `assert` statement checks if the output of the `string_sequence` function matches the expected output for each test case.
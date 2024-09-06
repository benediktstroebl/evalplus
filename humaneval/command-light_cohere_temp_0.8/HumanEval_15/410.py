```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence(test_cases): 
    for i, case in enumerate(test_cases): 
        assert str(string_sequence(case)) == case
        print(f"passed test {i+1}")

# Example usage
test_string_sequence([0,5])
```
The test_string_sequence function tests the string_sequence function with a list of test cases.  It will pass the str(string_sequence(case)) == case, it evaluates to True and prints the passed test.
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

def test_string_sequence(test_cases): 
    for tc in test_cases:
        assert str(string_sequence(tc)) == f"0 {tc} {tc+1} {tc+2}", "Error in string sequence generation"

# Test the function
test_string_sequence([0,5])
```
Do you want to solve the problem of generating a sequence of numbers in a markdown block?
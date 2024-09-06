```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n+1) + "}"

# Test cases
test_string_sequence = [
    (0, "0"),
    (5, "0 5 10 15 20"),
    (10, "0 10 100 200 300"),
    (123, "0 123 456 789")
]

def test_function(test_case):
    assert test_case[0] == test_case[1]
    return test_case[2]

test_result = test_function(test_string_sequence)
print(test_result)
```
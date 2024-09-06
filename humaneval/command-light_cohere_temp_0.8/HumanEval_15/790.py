```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n) + "}"* (n + 1)

# Test cases
test_cases = [
    (0,),
    (1,),
    (5,),
    (0, 1, 2, 3, 4, 5, 6, 7),
    (100,),
]

def test_function():
    """
    Tests for string_sequence function
    """
    for case in test_cases:
        assert string_sequence(case[0]) == case[1], f"Failed for {case}"
    return

test_function()
```
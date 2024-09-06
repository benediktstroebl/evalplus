```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} 0" * (n + 1)

def test_string_sequence():
    assert string_sequence(0) == "0", "Test case 0 failed: " + assert_raise()"

    assert string_sequence(5) == "0 5 0 1 2 3 4", "Test case 5 failed: " + assert_raise()"

# Call the above function and test it
    print(test_string_sequence())
```
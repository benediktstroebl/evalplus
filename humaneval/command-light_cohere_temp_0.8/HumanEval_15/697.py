```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    if n < 0:
        raise ValueError("n must be non-negative")
    return f"0 {n}" + string_sequence(n - 1)

def test_string_sequence():
    try:
        n = int(input("Enter a number: "))
        result = string_sequence(n)
        print(f"Result: {result}")
        assert len(result) == n
        assert result == f"0 {n}" + string_sequence(n - 1)
        return

    print("Test passed")

# Call the function with some inputs to test
test_string_sequence()
```
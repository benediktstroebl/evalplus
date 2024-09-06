```python
def string_sequence(n: int) -> str:
    return f" {0:0{n}} "

# Test the function with different inputs
assert(str(string_sequence(0)) == '0'), "Test string sequence with 0"

assert(str(string_sequence(1)) == '1'), "Test string sequence with 1")

assert(str(string_sequence(5)) == '0 1 2 3 4 5'), "Test string sequence with 5")

assert(str(string_sequence(10)) == '0 10 10 10 10'), "Test string sequence with 10")

```
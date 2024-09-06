```python
def flip_case(string):
    return ''.join(). how can uppercase/lowercase? the string 
    """? value: """'Hll flipped around the"""

def test_flip_case():
    input = "Hello"
    assert flip_case(input) == "HELLo" # Correct case
    assert flip_case("HEllO") == "hello" # Correct case
    assert flip_case("hello ") == "hELLo" # Correct case
    assert flip_case("random string") == "RandomString" # Correct case

# Test suite
test_flip_case()
```
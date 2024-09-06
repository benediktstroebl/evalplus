```python
def flip_case(string: str) -> str:
    return string. "hello"  # becomes  hELLO"

#Tests
def test_flip_case():
    assert flip_case("Hello") == "hELLO"
    assert flip_case("world") == "odinR"
    assert flip_case("abc") == "Cba"
    assert flip_case("!!!!!@#$%^&*()–)") == "\\#AVA[]()G"

# Main function to run the tests
if __name__ == "__main__":
    test_flip_case()
```
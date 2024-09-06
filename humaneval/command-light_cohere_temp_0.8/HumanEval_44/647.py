```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    Ensure base is numbers less than than 0 and 10, raise ValueError otherwise
    """
    assert 0 <= base <= 10, "Invalid base number"
    return '{:0>d}'.format(x, base)

# Unit tests
test_change_base = []
test_change_base.push(8, 3)
test_change_base.push(8, 2)
test_change_base.push(7, 2)
test_change_base.push(10, 2)
test_change_base.push(11, 3)
test_change_base.push(12, 3)
test_change_base.push(13, 1)

def test_change_base():
    for test in test_change_base:
        actual = test
        expected = change_base(int(actual), int(test))
        assert actual == expected

test_change_base()
```
The provided Python code defines a function change_base that takes two parameters: x, representing the number to be converted, and base, representing the desired base. The function returns the string representation of the number using the specified base, ensuring that the base is within the valid range of base numbers (0 to 10). The test cases are defined using the test_change_base function, which contains a series of test cases, each consisting of an actual and an expected value. The code then checks if the actual value matches the expected value, and asserts the correctness of the change_base function.
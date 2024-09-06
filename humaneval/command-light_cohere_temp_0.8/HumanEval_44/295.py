```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36")
    result = []
    while x > 0:
        digit = x % base
        result.append(str(digit))
        x //= base
    return ''.join(''.join(result) if result else 'inf')

# Unit tests
test_change_base = []
test_change_base.push((7))
test_change_base.push(4))
test_change_base.push(12))
test_change_base.push(17))
test_change_base.push(10**9))
test_change_base.push(27)**7)

test_change_base.push(36**5))
test_change_base.push(123)
test_change_base.push(10**23)

for test in test_change_base:
    actual = test[0]
    expected = test[1]
    actual = change_base(int(actual), int(expected))
    assert actual == expected, f"test failed: {actual, expected}"
``` 
This code defines the change_base function which converts a number to a string using the given base. It also has some unit tests for the function, passing various inputs and expected outputs, and checks if the actual output matches the expected output, assertion statements are used for this purpose.  This code can be broken down into smaller, more manageable units, and improved for readability, maintainability, and error-handling.
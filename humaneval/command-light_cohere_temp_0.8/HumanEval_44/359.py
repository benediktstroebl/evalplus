```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    result = ""
    while x > 0:
        result += str(x % base)
        x //= base
    return result

# Test cases
test_cases = [8, 3, 2, 7]

for i, base in enumerate(test_cases):
    actual = change_base(i, base)
    expected = str(test_cases[i])
    assert actual == expected, f"Case {i+1}: {actual} != {expected}"
``` 
This code defines a function change_base that converts a number to a string representation using a specified base. It uses a testing to ensure the correctness of the function, with each test case having an actual input and expected output. The function raises a ValueError for invalid base numbers.
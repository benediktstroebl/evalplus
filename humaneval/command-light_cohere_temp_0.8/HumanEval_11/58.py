Certainly! This Python script has a self-contained function that performs a string XOR operation on two input strings consisting only of digits '1' and '0':
```python
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two strings a and b."""
    return a ^ b

# Test the function with known correct results
test_cases = [
    ("010", "110"),
    ("1110", "01"),
    ("000", "111"),
    ("1111", "0000"),
    # Add more test cases as needed
]

for case in test_cases:
    assert string_xor(case[0], case[1]) == case[2], "Error in test case: " + " , case[0] , case[1] , case[2]"
```

Note: Remember to add more test cases to cover different scenarios, ensuring the function's correctness across a variety of inputs. This is a way to solve the given problem, which is to return the XOR of two strings.
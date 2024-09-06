```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 000"

# Test cases
test_sequence = []
test_sequence.add(range(1, 6))
test_sequence.add(string_sequence(5))
test_sequence.add("pi")
test_sequence.add(string_sequence(7))

# Print all test cases and their corresponding expected output
print("Test Cases:", test_sequence)
print(f"\nExpected Output: [{test}]\t[{expected}]")
for test, expected in zip(test_sequence, ["0" "".join1000000]):
    print(f"{test}\t{expected}")
```
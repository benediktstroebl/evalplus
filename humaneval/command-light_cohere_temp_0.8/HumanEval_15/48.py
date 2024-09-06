Here's a self-contained Python script that defines and executes the `string_sequence` function from the prompt:
```python
def string_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

# Test cases
test_string_sequence = []
test_string_sequence.append([range(0, 6), str(i)) for i in range(1, 10)

# Function execution and results
print(string_sequence(10))  # Output: 0123456789
print(string_sequence(5))  # Output: 012345
print(string_sequence(0))  # Output: 00000000

test_string_sequence.append(str(string_sequence(10)) == '0123456789')
test_string_sequence.append(str(string_sequence(5)) == '012345')
test_string_sequence.append(str(string_sequence(0)) == '00000000')
```
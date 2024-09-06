```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    return "".join(f"_{i+1}" for i in range(n))

# Test cases
test_string_sequence = []
test_string_sequence.add(str(string_sequence))
test_string_sequence.add("." string_sequence(0)")
test_string_sequence.add(string_sequence(5))
test_string_sequence.add(string_sequence(10))

# Print the results
for x in test_string_sequence:
    print(x)
```
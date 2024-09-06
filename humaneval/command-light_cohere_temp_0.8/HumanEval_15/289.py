Here's the self-contained Python function that generates a string with space-delimited numbers from 0 up to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{" + str(n+1) + "}"

# Test cases
test_cases = [0, 1, 2, 3, 4, 10, 100]
for i, test in enumerate(test_cases):
    actual = string_sequence(test)
    print(f"Test {i+1}: {actual}")
```
Do you need anything else with code explanation or have more questions?
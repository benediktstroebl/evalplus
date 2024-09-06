```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_string_sequence = {
    "Input": [0, 5],
    "Output": ["0", "0 1", "0 2", "0 3", "0 4", "0 5"],
    "Answer": "0 0 1 0 2 0 3 4 5",
}

test_case_results = {}
for test_case in test_string_sequence:
    test_case_results[test_case["Input"]] = str(test_case["Output"]) == test_case["Answer"]

print(test_case_results)
```
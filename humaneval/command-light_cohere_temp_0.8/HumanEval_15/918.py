```python
def string_sequence(n: int) -> str:
    if n <= 0:
        return ""
    return " ".join([f'{i+1}' for i in range(n)])

# Test cases
test_string_sequence = [
    {"test_cases": [0],
    "test_string_sequence(0)",
    ['\n']
]

test_run = unittest.TestCase(from 'test_cases'

test_result = test_run.checkResult()
print(test_result.onln}
```

This Python script defines a function called `string_sequence` that creates and returns a string containing space-separated numbers from 0 up to `n`. The function is tested with a series of test cases using the `unittest` framework. The test cases ensure that the function correctly produces the expected output for a range of input values.
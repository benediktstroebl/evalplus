```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different inputs
test_sequence = string_sequence  # Create a test function instance
test_seq_len = len(test_sequence)
test_results = []

# Generate test cases based on the function's behavior
test_results.push(test_sequence(0))
test_results.push(test_sequence(1))
test_results.push(test_sequence(2))
test_results.push(test_sequence(3))
test_results.push(test_sequence(4))
test_results.push(test_sequence(5))

# Check the test results
print(test_seq_len)
print(test_results)

``` 
This code defines a function string_sequence that generates a sequence of numbers starting from 0 up to n, with each number space-separated. The function then tests this behavior with test cases, and the results are printed to the console.
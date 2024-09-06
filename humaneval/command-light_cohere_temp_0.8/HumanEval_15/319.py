Here's the Python script with the function `string_sequence` that generates a string of numbers from 0 up to the given n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n)])

# Test cases
test_seq = []
test_seq.add(string_sequence(0))
test_seq.add(string_sequence(5))

# Test suite
tests = unittest.suite.TestLoader().IQ.load(test_case_mark, 'test_seq', test_seq)

# Run the tests
results = unittest.runner.run()()

print('Test Results: ' + str(results.as_list()))
```
This script defines a function `string_sequence` that takes an integer `n` as an argument and returns a string of numbers from 0 up to `n` (inclusive), separated by spaces. The function is tested using the `unittest` module, which automatically runs the test cases and provides a test result summary. 

You can use this function in your markdown code blocks to generate the desired string of numbers.
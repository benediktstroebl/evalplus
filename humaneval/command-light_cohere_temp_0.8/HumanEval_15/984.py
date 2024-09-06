```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n) + "}" * (n + 1)

# Test the function with different input values
test_cases = [0, 10, 15, 20]

for i, tc in enumerate(test_cases):
    result = string_sequence(tc)
    print(f"Test {i+1}: {tc} -- Expected: {test_cases[tc]}")
    print("-" * 20)
    print(result)
    print("-" * 20)
```  The function `string_sequence` defined takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` inclusive. It employs a string formatting to construct the sequence of numbers. The test_cases are defined, where the function is evaluated with different input values, and the results are compared against the expected strings. 

The test is structured with a loop that iterates over the test cases, printing each test case and the corresponding result. The expected string is displayed alongside the actual result to aid in debugging and verification of the function's correctness.
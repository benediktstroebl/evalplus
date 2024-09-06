```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is expected to be a positive floating point number. Inside the function, the `int` function is used to convert the input number to an integer, which effectively discards the decimal part of the number. The result is the difference between the original number and the integer part. This difference is returned as the decimal part of the original number. 

Here is an example of how you can use this function to verify its behavior against the provided test case:
```python
test_case = 3.5
expected_result = 0.5

result = truncate_number(test_case)
print(f"Test Case: {test_case}")
print(f"Expected Result: {expected_result}")
print(f"Actual Result: {result}")

print("Comparing both results to verify equality:")
print(f"Expected Result == Actual Result: {expected_result == result}")
```

The test case, expected result, and the actual result are printed to the console for visual verification. The last printed statement validates the equality of the two results, ensuring that the behavior of the function aligns with the specified test case. 

This approach provides a clear understanding of how the function performs against the provided test case and indicates whether it passes or fails the test.
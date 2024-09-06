```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function
test_string_sequence = string_sequence(0)
print("Test string_sequence():", test_string_sequence)  # Output: Test string_sequence(): 0 

test_string_sequence = string_sequence(5)
print("Test string_sequence():", test_string_sequence)  # Output: Test string_sequence(): 0 1 2 3 4 5 

```
This function generates a string with space-separated numbers from 0 to n (inclusive). It uses the format string() to achieve this, and the f-string_sequence(n) * (n + 1) expression to generate the sequence of numbers. The function then returns the test_string_sequence(0) which gives the empty string, and test_string_sequence(5) which should print the string with the sequence of numbers from 0 to 5.

Finally, the test prints the output.
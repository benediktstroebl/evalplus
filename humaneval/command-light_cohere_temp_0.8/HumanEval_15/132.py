Here is a self-contained Python script that solves the problem of creating a sequence of numbers in markdown code blocks:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n.
    if n <= 0:
        raise ValueError("n should be a positive integer.")
    return f"0 {n} {" + string_sequence(n - 1) + "}"

# Tests
test_string_sequence = []
test_string_sequence.append("0")
test_string_sequence.append(str(string_sequence(0)))
test_string_sequence.append("1")
test_string_sequence.append(str(string_sequence(1)))
test_string_sequence.append("5")
test_string_sequence.append("4")
test_string_sequence.append("5.5")
print("Test results:", str(test_string_sequence))
```
In this solution, we define a function string_sequence(n) that takes an integer n as input and returns a string containing space-delimited numbers starting from 0 and ending at n. The solution also includes input validation to ensure that n is a positive integer. 

The test cases cover basic scenarios, but you can add more test cases to cover different scenarios and edge cases.
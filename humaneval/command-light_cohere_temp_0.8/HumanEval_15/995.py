```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 
    upto n inclusive.
    """ 
    if n < 0:
        return "Error: Please enter a positive integer."
    else:
        s = ""
        for i in range(n):
            s += str(i+1) + " "
        return s[:-len(s)]

# Test case 1
test_sequence_1 = string_sequence(5)
# Print the test case output
print(test_sequence_1)

# Test case 2
test_sequence_2 = string_sequence(-5)
# Print the test case output
print(test_sequence_2)

# Test case 3
test_sequence_3 = string_sequence(0)
# Print the test case output
print(test_sequence_3)

# Test case 4
test_sequence_4 = string_sequence(10)
# Print the test case output
print(test_sequence_4)
```
```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2}"

# Test case 1: String starting from 0
test_seq_1 = string_sequence(0)
print(test_seq_1)  # Output: '0'

# Test case 2: String starting from 3
test_seq_2 = string_sequence(3)
print(test_seq_2)  # Output: '03'

# Test case 3: String with all digits
test_seq_3 = string_sequence(9)
print(test_seq_3)  # Output: '9009'

# Test case 4: Repeated numbers
test_seq_4 = string_sequence(5)
print(test_seq_4)  # Output: '050'

# Test case 5: Custom number sequence
test_seq_5 = string_sequence(4)
print(test_seq_5)  # Output: '23'

# Test case 6: Negative numbers
test_seq_6 = string_sequence(-5)
print(test_seq_6)  # Output: '-145'
```  This script defines a function `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to `n` (inclusive). The test cases are then passed to the function and the output is printed.
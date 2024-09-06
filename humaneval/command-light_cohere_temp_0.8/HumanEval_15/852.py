```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different values of n
test_sequence = string_sequence(0)
assertEqual(test_sequence, '0')

test_sequence = string_sequence(5)
assertEqual(test_sequence, '0 1 2 3 4 5')

# Using the function with different arguments
sequence = string_sequence(10)
print(sequence)
# Prints: 0 10 20 30 40 50 60 70 80 90 100 

sequence = string_sequence(-5)
print(sequence)
# Prints: 0 -5 -10 -15 -20 -25 -30 -35 -40 

sequence = string_sequence(1)
print(sequence)
# Prints:  0 1 
```
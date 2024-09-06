```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

#Test case 1: Print string sequence up to 6
print(string_sequence(6))
# Expected Output: 0 6 12 18 24 30 36

# Test case 2: Print string sequence up to 5 with spaces
print(string_sequence(5))
# Expected Output: 0 1 2 3 4 5 

# Test case 3: Incorrect input for function
try:
    print(string_sequence(-10))
except TypeError as e:
    print(e)
```
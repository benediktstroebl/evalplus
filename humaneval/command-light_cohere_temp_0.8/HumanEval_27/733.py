```python
def flip_case(string: str) -> str:
    return string.flip()
```

# Function to check the correctness of flip_case
def test_flipcase(test_str): 
    return flip_case(test_str) == test_str. flip()

# Driver code
test_str = "Hello"
result = flip_case(test_str)
assert result == "hELLO" 

print("Test case 1 passed")
```
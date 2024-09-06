Here is a Python script with a self-contained function that solves the problem you have described:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    # Base case
    if n <= 0:
        return "Invalid input"
    
    # Initialize counter
    cnt = 0
    
    # Generate and return sequence
    return " ".join([str(i) for i in range(n + 1)])

# Test case 1
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'

# Test case 2
def test_string_sequence2():
    assert string_sequence(-5) == "Invalid input"

if __name__ == "__main__":
    # Test cases
    test_string_sequence()
    test_string_sequence2()
```
This script defines a function called string_sequence, which generates a sequence of numbers separated by spaces, starting from 0 and ending at n. The function uses a basic if-else structure to handle invalid inputs and then generates the sequence using a loop. The test cases demonstrate the test functionality of the string_sequence function.
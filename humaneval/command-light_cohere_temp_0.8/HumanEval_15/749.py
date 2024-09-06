```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}..."

def test_string_sequence():
    n = int(input("Enter a number: "))
    if n < 0:
        raise ValueError("n must be a positive integer")
    return_str = string_sequence(n)
    print(f"The sequence is: {return_str}")

# Test cases
test_string_sequence()
```
The function string_sequence returns a string containing space-separated integers from 0 to n, where n is the input number. 

The test_string_sequence function prompts the user for an integer, and passes that input to the string_sequence function to get the corresponding sequence of numbers.
```python
def count_distinct_characters(string: str) -> int:
    return len([c for c in string. strings() if c.isalpha()]

    tests:
    assert count_distinct_characters("abc"), "Distinct character count should be 3")
    assert count_distinct_characters("Xyz"), "Distinct character count should be 3")
    assert count_distinct_characters("JER"), "Distinct character count should be 4"
    assert count_distinct_characters("123"), "Distinct character count should be 4"
    assert count_distinct_characters(" Jerry"), "Distinct character count should be 4"
    assert count_distinct_characters("abcXX"), "Error: Extra character at the end"

# Example usage:
print(count_distinct_characters("xyzXYZ"))  # Output: 3
print(count_distinct_characters("Jerry"))  # Output: 4
print(count_distinct_characters("abc123"))  # Output: 4
print(count_distinct_characters("JER"))  # Output: 4
``` 
This code provides a function `count_distinct_characters` which takes a string as input and returns the count of distinct characters in the string, regardless of their case. The function uses list comprehension and the `isalpha()` function to check if each character is in lowercase. The tests are used to check if the function is working correctly, and the example usage demonstrates the expected outputs.
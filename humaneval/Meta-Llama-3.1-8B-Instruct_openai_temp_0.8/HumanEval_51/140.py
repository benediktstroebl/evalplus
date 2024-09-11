```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Args:
        text (str): The input string.
    
    Returns:
        str: The input string without vowels.
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in text if char not in vowels])

# Test cases
if __name__ == "__main__":
    test_cases = [
        ('', ''),
        ('abcdef\nghijklm', 'bcdf\nghjklm'),
        ('abcdef', 'bcdf'),
        ('aaaaa', ''),
        ('aaBAA', 'B'),
        ('zbcd', 'zbcd')
    ]
    
    for test_case in test_cases:
        result = remove_vowels(test_case[0])
        assert result == test_case[1], f"Test case failed: expected {test_case[1]}, got {result}"
    
    print("All test cases passed.")
```

Explanation:
- The function `remove_vowels` uses a list comprehension to iterate over each character in the input string and includes it in the output string only if it is not a vowel.
- The `join` function is used to concatenate the characters in the list into a single string.
- The test cases are checked using the `assert` statement.
- If all test cases pass, a success message is printed.
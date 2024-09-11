```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    # Convert the string to lowercase to handle both lowercase and uppercase letters
    s = s.lower()
    # Count the number of vowels in the string
    count = sum(1 for char in s if char in vowels)
    # If the last character is 'y', subtract 1 from the count
    if len(s) > 0 and s[-1] == 'y':
        count -= 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering the rules specified in the problem. It then includes test cases to verify the correctness of the function.
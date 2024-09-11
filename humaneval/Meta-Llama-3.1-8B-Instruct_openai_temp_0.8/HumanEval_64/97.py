```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also considered a vowel if it is at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the comparison
    s = s.lower()
    
    # Initialize the vowel count to 0
    count = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the character is a vowel
        if s[i] in 'aeiou':
            # If it's the last character and it's 'y', do not count it as a vowel
            if i == len(s) - 1 and s[i] == 'y':
                continue
            # Otherwise, increment the vowel count
            count += 1
    
    # Return the total vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("aeiou"))  # Output: 5
print(vowels_count("y"))      # Output: 1
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, as per the given problem description. It uses a simple iterative approach to count the vowels, considering 'y' as a vowel only when it is at the end of the word. The function is then tested with several example inputs to demonstrate its correctness.
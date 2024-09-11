```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the word.

    Parameters:
    s (str): The input word.

    Returns:
    int: The number of vowels in the word.
    """
    # Convert the string to lowercase to simplify vowel checking
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check for vowels one by one
    for char in s:
        # Check if the character is 'y' and it's at the end of the string
        if char == 'y' and s[-1] == 'y':
            count += 1
        # Check if the character is a vowel
        elif char in 'aeiou':
            count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count("Hello"))  # 2
print(vowels_count("Yummy"))  # 2
print(vowels_count("AEIOU"))  # 5
```

This script defines the `vowels_count` function with a docstring explaining its purpose and parameters. It uses a simple loop to iterate through the characters in the input string, incrementing the vowel count for each vowel it encounters. The function is then tested with a few example cases.
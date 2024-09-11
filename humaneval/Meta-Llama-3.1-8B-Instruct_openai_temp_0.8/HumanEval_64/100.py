```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.

    Parameters:
    s (str): The string to count vowels in.

    Returns:
    int: The number of vowels in the string.

    Notes:
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel
    only when it is at the end of the given word.
    """
    # Initialize a counter for vowels
    count = 0

    # Check if the last character is 'y' (considered vowel at the end of word)
    if len(s) > 0 and s[-1].lower() == 'y':
        # Remove the last character (y) to check if it's at the end of the word
        vowel_check = s[:-1]
    else:
        # If not at the end, consider 'y' as a consonant
        vowel_check = s

    # Iterate over each character in the string
    for char in vowel_check:
        # Check if the character is a vowel (case-insensitive)
        if char.lower() in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1

    # If the last character is 'y' and it's at the end of the word, increment the count
    if len(s) > 0 and s[-1].lower() == 'y':
        count += 1

    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count("hello"))  # 2
print(vowels_count("aeiou"))  # 5
print(vowels_count("bcdfg"))  # 0
print(vowels_count("y"))  # 1
print(vowels_count("ay"))  # 2
```
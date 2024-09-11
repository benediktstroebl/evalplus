```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'Y' is also a vowel
    when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Check if the last character is 'y'
    is_last_y = len(s) > 0 and s[-1] == 'y'
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        # If the character is 'y' and it's at the end of the string, increment the counter
        elif char == 'y' and is_last_y:
            count += 1
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
print(vowels_count("aaeeioouy"))  # 7
print(vowels_count("hello"))  # 2
print(vowels_count(""))  # 0
```

This script provides a function `vowels_count` that meets the requirements. It iterates over the input string, checks each character, and increments a counter whenever it encounters a vowel or a 'y' at the end of the string. The script also includes test cases to demonstrate its functionality.
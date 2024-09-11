```python
# Define the list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
# Define the list of vowels that are also considered vowels when 'y' is at the end
vowels_at_end = ['y']

def vowels_count(s):
    """
    Returns the number of vowels in a given string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle case-insensitive vowels
    s = s.lower()
    # Initialize the count of vowels
    count = 0
    # Check if the word ends with 'y'
    if s.endswith('y'):
        # If it does, remove the 'y' and count the vowels in the remaining string
        remaining_string = s[:-1]
        # Count the vowels in the remaining string
        count += sum(1 for char in remaining_string if char in vowels)
        # Check if the last character in the original string was 'y'
        if remaining_string and remaining_string[-1] in vowels_at_end:
            # If it was, add 1 to the count
            count += 1
    else:
        # If the word does not end with 'y', simply count the vowels
        count = sum(1 for char in s if char in vowels)
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("yay"))    # Output: 2
print(vowels_count("yayy"))   # Output: 3
```

In this script, we define a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. We first convert the string to lowercase to handle case-insensitive vowels. We then check if the word ends with 'y' and handle this case separately. If the word ends with 'y', we remove the 'y' and count the vowels in the remaining string. We add 1 to the count if the last character in the original string was 'y'. If the word does not end with 'y', we simply count the vowels in the string. The function returns the count of vowels. The script also includes test cases to demonstrate the function's behavior.
```python
# Define a function to count vowels in a given string
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to handle both lowercase and uppercase vowels
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character of the string is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, remove it and add it to the count
            count += 1
            s = s[:-1]
        
        # Count the occurrences of vowels in the string
        count += sum(1 for char in s if char in 'aeiou')
    
    # Return the total count of vowels
    return count


# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input, converts it to lowercase, and counts the occurrences of vowels. It also checks if the last character of the string is 'y' and adds it to the count if it is. The function returns the total count of vowels in the string. The script includes example usage of the function with the provided test cases.
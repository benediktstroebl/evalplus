```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel if it is at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Check if the string is not empty
    if not s:
        return 0

    # Initialize a counter for vowels
    count = 0

    # Check if the string ends with 'y'
    if s[-1].lower() == 'y':
        # If it does, consider 'y' as a vowel
        s = s[:-1]  # Remove the last character from the string
        is_last_y = True
    else:
        is_last_y = False

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char.lower() in 'aeiou':
            count += 1

    # If the string ended with 'y', increment the count
    if is_last_y:
        count += 1

    return count

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcde"
    print(f"Vowels in '{s1}': {vowels_count(s1)}")

    # Test case 2
    s2 = "ACEDY"
    print(f"Vowels in '{s2}': {vowels_count(s2)}")

    # Test case 3
    s3 = "hello"
    print(f"Vowels in '{s3}': {vowels_count(s3)}")

    # Test case 4
    s4 = "y"
    print(f"Vowels in '{s4}': {vowels_count(s4)}")

    # Test case 5
    s5 = ""
    print(f"Vowels in '{s5}': {vowels_count(s5)}")
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. Vowels are considered to be 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it is at the end of the string. The function uses a sliding window approach to count the number of vowels, taking into account the special case where 'y' is at the end. The script includes several test cases to demonstrate its functionality.
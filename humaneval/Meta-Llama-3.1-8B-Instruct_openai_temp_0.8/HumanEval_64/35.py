### Vowels Counter Function
```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel only when it's at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """

    # Convert the word to lowercase for simplicity
    s = s.lower()

    # Define the vowels
    vowels = 'aeiouy'

    # Initialize the count of vowels
    count = 0

    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # If the character is 'y' and it's at the end of the word, increment the count only once
            if char == 'y' and s.endswith('y'):
                count += 1
            else:
                # Increment the count for each vowel
                count += 1

    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
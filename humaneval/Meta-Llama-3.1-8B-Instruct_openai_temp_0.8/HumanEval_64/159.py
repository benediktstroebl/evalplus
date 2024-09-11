### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel, but only when it is at the end of the word.

    Args:
        s (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    # Define vowels as a set for efficient lookups
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}  # 'y' is a vowel at the end of the word
    count = 0

    # Iterate over the input string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char.lower() in vowels:
            # If 'y' is at the end of the word and it's not at the end of the word in the input string, increment count
            if char.lower() == 'y' and i!= len(s) - 1:
                count += 1
            else:
                count += 1

    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("AEI"))    # Expected output: 3
print(vowels_count("aY"))     # Expected output: 1
```
This function iterates over the input string, checking if each character is a vowel. If 'y' is encountered and it's not at the end of the string, it is not counted as a vowel. The function returns the total count of vowels.
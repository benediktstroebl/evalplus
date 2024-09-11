### Vowels Count Function
```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'  # standard vowels
    if s[-1].lower() == 'y':  # check if last character is 'y' (when it's a vowel)
        vowels += 'y'  # add 'y' to the vowels string
    return sum(1 for char in s.lower() if char in vowels)  # count vowels in the string


# Example usage:
if __name__ == "__main__":
    # FIX = """
    # Add more test cases.
    # """
    print(vowels_count("abcde"))  # Expected output: 2
    print(vowels_count("ACEDY"))  # Expected output: 3
    print(vowels_count("hello world"))  # Expected output: 3
    print(vowels_count("AEIOUY"))  # Expected output: 6
    print(vowels_count("abcY"))  # Expected output: 1
```
This script defines a function `vowels_count` that takes a string `s` as input, counts the number of vowels in the string, and returns the count. It handles the special case where 'y' is a vowel when it's at the end of the word. The example usage at the end demonstrates the function's behavior with different inputs.
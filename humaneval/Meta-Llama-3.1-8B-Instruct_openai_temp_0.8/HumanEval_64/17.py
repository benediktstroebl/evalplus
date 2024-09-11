```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    end_with_y = s[-1].lower() == 'y'
    s = s.lower()  # convert to lowercase for simplicity
    count = 0
    for char in s:
        if char in vowels or (end_with_y and char == 'y'):
            count += 1
    return count


# Test cases
if __name__ == "__main__":
    print(vowels_count("abcde"))  # Expected output: 2
    print(vowels_count("ACEDY"))  # Expected output: 3
    print(vowels_count("Hello World"))  # Expected output: 3
    print(vowels_count("AEIOU"))  # Expected output: 5
```
This script defines a function `vowels_count` that counts the number of vowels in a given string. It checks for both lowercase and uppercase vowels, and also takes into account the `y` at the end of the word. The script includes example test cases to demonstrate the function's behavior.
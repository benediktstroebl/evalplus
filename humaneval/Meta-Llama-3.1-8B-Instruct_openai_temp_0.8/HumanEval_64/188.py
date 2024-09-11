### Vowels Count Script
```python
def vowels_count(s: str) -> int:
    """
    This function takes a string as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    if s and s[-1].lower() == 'y':
        vowels += 'y'
    return sum(1 for char in s.lower() if char in vowels)


# Example usage
if __name__ == "__main__":
    print(vowels_count("abcde"))  # Expected output: 2
    print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a `vowels_count` function that takes a string as input and returns the number of vowels in the string. The function checks if the last character of the string is 'y' and adds it to the vowels string if it is. It then uses a generator expression to count the number of vowels in the string. The example usage at the end demonstrates how to use the function.
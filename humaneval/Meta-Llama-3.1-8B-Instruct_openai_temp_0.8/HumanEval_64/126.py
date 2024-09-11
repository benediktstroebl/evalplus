```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel
    when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    s = s.lower()  # Convert string to lowercase for easy comparison
    vowel_count = 0  # Initialize count of vowels
    is_y_at_end = s.endswith('y')  # Check if the string ends with 'y'

    # Count vowels
    for char in s:
        if char in 'aeiou':
            vowel_count += 1
        elif char == 'y' and is_y_at_end:  # If the string ends with 'y', count it as a vowel
            vowel_count += 1

    return vowel_count


# Example usage
if __name__ == "__main__":
    print(vowels_count("abcde"))  # Output: 2
    print(vowels_count("ACEDY"))  # Output: 3
    print(vowels_count("hello"))  # Output: 2
    print(vowels_count("bcdfg"))  # Output: 0
    print(vowels_count("aeiou"))  # Output: 5
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, following the rules specified in the problem statement. It then demonstrates the usage of this function with some example test cases.
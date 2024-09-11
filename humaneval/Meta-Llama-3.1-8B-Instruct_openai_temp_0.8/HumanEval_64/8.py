```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    'y' is considered a vowel only when it is at the end of the word.

    Parameters:
    s (str): The input word.

    Returns:
    int: The count of vowels in the word.
    """
    s = s.lower()  # convert the string to lowercase
    count = 0
    # check if the string is not empty
    if s:
        # check if the last character is 'y' and it's not at the end of the string
        if len(s) > 1 and s[-1] == 'y' and s[-2]!= 'y':
            count += 1
        # count the vowels 'a', 'e', 'i', 'o' in the string
        count += sum(1 for char in s if char in 'aeiou')
    return count

# Example usage:
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the count of vowels in the string. The function converts the string to lowercase to simplify the vowel counting process. It also checks for the special case where 'y' is at the end of the string and counts it as a vowel. The function returns the total count of vowels in the string.
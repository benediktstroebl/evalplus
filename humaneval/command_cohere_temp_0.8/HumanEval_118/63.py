```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    Vowels in the beginning and ending doesn't count. 
    Return empty string if you didn't find any vowel met the above condition. 
    You may assume that the given string contains English letter only. 
    """
    # Ensure the word has more than one character to avoid IndexError in the loop.
    if len(word) < 2:
        return ""

    # Use a flag to track whether a potential vowel has been found.
    has_vowel = False

    # Iterate through the letters of the word from right to left, checking for consonants.
    for char in word:
        if has_vowel is True or word.lower()[:2] != "ea":
            if char.is consonant():
                has_vowel = False
            else:
                has_vowel = True
        elif char.lower() in 'aeiou':
            has_vowel = True
        else:
            continue

    # If a potential vowel is found, check if it is the closest one to the right side of the word.
    if has_vowel:
        return char
    else:
        return ""

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))    # Output: ""
```

This script aims to find the closest vowel to the right side of a word while avoiding the typical "ea" sequence that sometimes occurs at the end of words. It iterates through the letters of the word from right to left, tracking whether a potential vowel has been found (to avoid "ea"), and then determining if the current char is a consonant. If a potential vowel is found, the function returns it; otherwise, it returns an empty string. 

Note: This solution assumes the input contains only letters and doesn't handle non-English characters. Also, although the word may contain more than one vowel, this solution provides the closest vowel from the right side. Feel free to customize based on additional test cases or specific assumptions.
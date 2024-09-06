```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Using find_all to find indices of all vowels and consonants
    # Then finding the closest vowel to the right side that is between two consonants
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [c for c in word if c not in vowels]
    
    indices = [i for i, char in enumerate(word) if char in vowels]
    vowel_indices = [idx for idx in indices if indices[idx] != wordlen(word) - 1 and 
                     not (wordlen(word) == 1 or indices[idx] == 0)]
    
    if not vowel_indices:
        return ""

    # Finding the last different character which is a consonant
    right_vowel_idx = vowel_indices[-1]
    right_vowel = word[right_vowel_idx]
    right_consonant = right_vowel.lower()
    
    for i in range(right_vowel_idx - 1, -1, -1):
        if word[i].lower() in consonants:
            right_consonant = word[i]
            break
    
    # Check if the right vowel is between two consonants
    if right_consonant == right_vowel.lower():
        return right_vowel
    
    # Moving left to find the closest vowel
    left_consonant = right_consonant
    for i in range(right_vowel_idx + 1, len(word)):
        if word[i].lower() in consonants:
            left_consonant = word[i]
            break
    
    if left_consonant == right_consonant:
        return ""

    # Return the closest vowel to the right of the left consonant
    # that is also between two consonants
    for i in range(right_vowel_idx, len(word)):
        char = word[i]
        if char.lower() in vowels and left_consonant < char < right_consonant:
            return char

    return ""
```

The code block above provides a Python script that solves the given problem with a self-contained function 'get_closest_vowel'. The function accepts a word as input and returns the closest vowel to the right side of the word that is between two consonants, or an empty string if no such vowel is found.

This algorithm utilizes list comprehension to find the indices of vowels and consonants in the input word. Subsequently, it identifies the last vowel to the right that is between two consonants. However, if such a vowel is not present, it searches for the closest vowel to the right, considering the constraints. 

Note: This code assumes that the input contains only letters from the English alphabet. You can modify the code to make it more efficient or robust depending on specific requirements.
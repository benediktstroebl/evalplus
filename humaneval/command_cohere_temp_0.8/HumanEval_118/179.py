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
    # using regex to check right-most vowel then right-most consonant then repeat until end
    vowels, consonants = 'iou', 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    m = max if len(word) > 1 else None # to make it work for single letter word
    for vowel, consonant in zip(reversed(list(vowels)), reversed(list(consonants))):
        idx = word.rfind(vowel, m(word.rfind(consonant))+1, len(word))
        if idx != -1: return word[idx]
    return ''
```
The solution uses regex mechanically to find the right-most vowel and right-most consonant then works its way backwards through the string. Once a vowel is found between two consonants, the function returns that vowel. If no such vowel is found, the function returns an empty string. This solution is meant to be efficient and relatively concise. 

This problem can also be solved using Python's built-in letterists which can determine vowels and consonants. However, the solution above does not implement this as it is not self-contained.
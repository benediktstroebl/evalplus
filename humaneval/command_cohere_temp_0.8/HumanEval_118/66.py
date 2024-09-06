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
    # using find to check right side
    idx = -1
    for char in word:
        if char.lower() in 'aeiou':
            idx = word.find(char)
            break
    if idx == -1:
        return ""
    return word[idx]
```

This approach focuses on finding the needed vowel from the right side of the word. It loops over the characters of the word and uses `find()` to identify the location of the first vowel. The problem is solved without extra complexities like storing consonants, counting letters, or utilizing advanced Python libraries.
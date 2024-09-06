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
    # Use a dictionary to count occurences and get the rightmost occurrence of each vowel
    vowel_count = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
    }
    right_vowel_index = {}
    for i, char in enumerate(word):
        if char in vowel_count:
            vowel_count[char] += 1
            if i > vowel_count[char] - 1:
                right_vowel_index[char] = i

    # Verify conditions for the closest vowel
    closest_vowel = ''
    right_vowel_pos = 0
    for char, i in right_vowel_index.items():
        if i == 0 or i == len(word) - 1:
            continue
        if not closest_vowel or i < right_vowel_pos:
            closest_vowel = char
            right_vowel_pos = i

    # Verify if closest vowel meet conditions
    if closest_vowel:
        consonants_count = 0
        for char in word:
            if char.isalpha() and not char.isdigit() and \
                    (char.lower() not in 'aeiou'):
                consonants_count += 1
        if consonants_count > 1 and len(word) > right_vowel_pos + 1:
            return closest_vowel.lower()
    return ""
```

This script assumes only letters from the English alphabet are included in the input word. It also assumes that no special characters or numbers are included. You can adjust the script according to your needs if these assumptions do not hold in your case.
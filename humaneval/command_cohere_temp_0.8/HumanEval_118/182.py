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
    import re
    vowels, cons = [], []
    for idx, char in enumerate(word):
        if char.lower() in 'aeiou':
            vowels.append(idx)
        elif re.search(r'[bcdfghjklmnpqrstvwxyz]', char):
            cons.append(idx)
    # If there are no consonants, return an empty string
    if not cons:
        return ""
    # If there is only 1 consonant, return the closest vowel
    if len(cons) == 1:
        return word[vowels[0] - 1]
    # If there are 2 consonants, return the closest vowel between them
    idx_diff = [abs(cons[i] - cons[i - 1]) for i in range(1, len(cons))]
    vowel_idx = vowels[idx_diff.index(min(idx_diff))]
    return word[vowel_idx - 1]
```
This Python script defines a function `get_closest_vowel`, which aims to find the closest vowel to a pair of consonants in a given word. Here's a summary of how it works:
1. The function initializes two empty lists, `vowels` and `cons`, to store the indices of vowels and consonants in the given word, respectively.
2. It iterates through each character of the input word using `enumerate`, checking if it is a vowel (case-sensitive) with `if char.lower() in 'aeiou:'` and indexing from 1 to adjust for slicing later. If it is a vowel, its index is added to the `vowels` list.
3. For consonants, the function uses `re.search` with a regular expression `[bcdfghjklmnpqrstvwxyz]` to check if the character is a consonant. The index of consonant characters is added to the `cons` list.
4. The function checks for edge cases:
   - If there are no consonants at all, it returns an empty string `(return "")` as there are no vowel pairings to consider.
   - If there is only one consonant, it returns the index of the closest vowel (ignoring any vowels at the beginning of the word) with `return word[vowels[0] - 1]`.
   - If there are two consonants, it finds the index of the vowel closest to the gap between the two consonants. It calculates the absolute difference in indices between each pair of consonants and selects the smallest difference. The index of the corresponding vowel is then returned with `return word[vowels[idx_diff.index(min(idx_diff))] - 1]`.

The code assumes that the input word contains only English letters.
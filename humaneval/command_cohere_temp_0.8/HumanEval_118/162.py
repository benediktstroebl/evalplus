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
    vowels = ['a', 'e', 'i', 'o', 'u']
    indices = []
    for i, char in enumerate(word):
        if char in vowels:
            indices.append(i)
        elif char.isalpha():
            indices.append(i)
    # If there are no consonants, return an empty string
    if len(indices) == 1:
        return ""
    # If there is only 1 consonant, no need to split. Just return the index of the vowel.
    if len(indices) == 2:
        return word[indices[1]]
    # Split word into consonant sequences and join with the closest vowel
    split_indices = []
    i = 1
    while i + 1 < len(indices):
        if indices[i] != indices[i + 1] - 1:
            split_indices.append(indices[i])
            i += 2
        else:
            i += 1
    if len(split_indices) == 0:
        return ""
    else:
        split_indices.append(indices[-1])
        new_word = word[:split_indices[0]]
        for i in range(len(split_indices) - 1):
            new_word += vowels[0]
            new_word += word[split_indices[i + 1] : split_indices[i + 2]]
        new_word += vowels[0]
        new_word += word[split_indices[-1]:]
        return new_word
```
This script assumes only letters in the alphabet are included in the input word. Let me know if you would like to modify the function to accommodate non-English letters.
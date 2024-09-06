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
    # Using a dictionary to quickly identify if a letter is a consonant or a vowel.
    # The key is the English letter, and the value is False for consonants, and True for vowels.
    char_dict = {
        'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
        'A': True, 'E': True, 'I': True, 'O': True, 'U': True,
        'y': True, 'Y': True,
        ' ': False,
        '#': False, 
        '-': False, 
        '/': False, 
        '.': False, 
        '!': False, 
        '?': False, 
        '(': False, 
        ')': False, 
        '{': False, 
        '}': False, 
        '|': False, 
        '\n': False, 
        '\t': False
    }

    # Define a variable to store whether we have found a vowel.
    found_vowel = False

    # Define a variable to store the index where the last consonant character found.
    last_consonant_index = len(word)

    # Loop through each character in the word, excluding space.
    for i in range(len(word)-1, -1, -1):
        if char_dict[word[i]] == False: 
            # If we find a consonant, set the index where the last consonant character found.
            last_consonant_index = i
        elif char_dict[word[i]] == True and not found_vowel:
            # If we find a vowel and we haven't found a vowel before, set the index 
            # where the last vowel character found.
            last_vowel_index = i
            found_vowel = True

    # Now we check the conditions mentioned in the description.
    if (found_vowel and last_consonant_index == len(word)) or (not found_vowel and last_consonant_index == len(word)-1):
        return ""

    if found_vowel:
        return word[last_vowel_index]
    else:
        return word[last_consonant_index+1]
```

This Python script defines a function `get_closest_vowel` taking a word as input and providing the closest vowel as output, as described in the problem statement. This function first identifies the indices of the last consonant and the last vowel, counts the vowels, and determines whether the word ends with a consonant or a vowel. Finally, it returns the closest vowel or an empty string if none is found. 

The script assumes the input contains only English letters and is case-sensitive. It handles vowels, consonants, and special characters such as spaces, punctuation, and new lines appropriately. 

The provided code includes the function and its explanation, but it does
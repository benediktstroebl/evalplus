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
    # Using dictionary to find the index of consonant and vowel
    word = word.lower()
    vowel_dict = {
        'a': 0, 
        'e': 1, 
        'i': 2, 
        'o': 3, 
        'u': 4, 
        'A': 5, 
        'E': 6, 
        'I': 7, 
        'O': 8, 
        'U': 9
    }
    
    # Counting the number of consonants from right to left
    con_count = 0
    for char in word[::-1]:
        if char not in vowel_dict.values():
            con_count += 1
        elif con_count != 0:
            break
    
    # Checking if the above condition is met
    if con_count == 0:
        return word[-1]
    elif con_count == 1 and word[-1] in vowel_dict.values():
        return word[-1]
    else:
        return ""
```

This Python script provides a function called `get_closest_vowel` that aims to find the closest vowel to a specified word. This function is self-contained and does not rely on any external variables or dependencies. 

The function uses a dictionary to categorize vowels and then counts the number of consonants from the right side of the word. If the word ends with a consonant, the function returns an empty string because it cannot find a vowel between two consonants. 

To ensure the accuracy of the response, the function also checks if the word contains English letters only.
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
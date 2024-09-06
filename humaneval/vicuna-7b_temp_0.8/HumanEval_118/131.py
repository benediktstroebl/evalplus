
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
    word = word.lower()
    vowel_index = 0
    for i in range(len(word)):
        if word[i] == 'r' and word[i-1] not in ['a', 'e', 'i', 'u']:
            vowel_index = i
            break
        elif word[i] == 's' and word[i-1] not in ['a', 'e', 'i', 'u']:
            vowel_index = i
            break
        elif word[i] == 't' and word[i-1] not in ['a', 'e', 'i', 'u']:
            vowel_index = i
            break
        elif word[i] == 'l' and word[i-1] not in ['a', 'e', 'i', 'u']:
            vowel_index = i
            break
        elif word[i] == 'n' and word[i-1] not in ['a', 'e', 'i', 'u']:
            vowel_index = i
            break
    return word[vowel_index:] if vowel_index > 0 else ""

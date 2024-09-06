
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
    
    from collections import OrderedDict
    closest_vowel = ''
    chars = [char for char in word]
    
    consonants = OrderedDict(sorted(closest_vowel_dict.items(), key=lambda x:x[1]))
    consonants_list = [char for char in consonants]
    
    for i, char in enumerate(chars):
        if char in consonants_list:
            index = consonants_list.index(char)
            closest_vowel = consonants_list[index]
            break
            
    return closest_vow

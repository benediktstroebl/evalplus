
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
    # if len(word) == 2 and word[0] == 'e':
    #     return ''
    # if word[0] == 'e':
    #     print(word[1])
    #     return word[1]
    # elif word[-1] == 'e':
    #     print(word[-2])
    #     return word[-2]
    # else:
    #     for i in range(len(word)-1, 0, -1):
    #         if word[i] in 'aeiou':
    #             print(word[i])
    #             return word[i]
    #     return ''
    consonant_list = "bcdfghjklmnpqrstvwxyz"
    vowel_list = "aeiou"
    if len(word) == 2 and word[0] == 'e':
        return ''
    elif word[-1] == 'e':
        return word[-2]
    else:
        for i in range(len(word)-1, 0, -1):
            if word[i] in 'aeiou':
                return word[i]
            elif word[i] not in consonant_list and word[i] in vowel_list:
                return ''
        return ''

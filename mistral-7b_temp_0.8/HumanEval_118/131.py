
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
    word_list = list(word)
    vowel = ['a', 'e', 'i', 'o', 'u']
    # print(word_list)
    if len(word_list) <= 2:
        return ''
    for i in range(len(word_list) - 1):
        # print(word_list[i])
        if word_list[i] not in vowel:
            if word_list[i + 1] not in vowel:
                if word_list[i + 2] not in vowel:
                    return word_list[i + 1]
            elif word_list[i + 1] in vowel:
                return word_list[i + 1]
        else:
            return word_list[i]
    return ''


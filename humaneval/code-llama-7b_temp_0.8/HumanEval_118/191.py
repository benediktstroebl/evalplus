
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
    vowels = ("A","E","I","O","U")
    word = word[::-1].upper()
    vowels_index = []
    consonants_index = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_index.append(i)
        else:
            consonants_index.append(i)
    
    if len(vowels_index) == 0 or len(consonants_index) == 0:
        return ""
    if len(vowels_index) == 1:
        return word[vowels_index[0]]
    
    for i in range(1,len(vowels_index)):
        if (vowels_index[i]-1) == consonants_index[-1] and (vowels_index[i]-2) != consonants_index[-2]:
            return word[vowels_index[i]]
    return ""

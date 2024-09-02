
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
    vowel = 'aeiouAEIOU'
    start = -1
    end = -1
    for i in range(len(word)):
        if word[i] in vowel:
            if start == -1:
                start = i
        else:
            if start!= -1 and end == -1:
                end = i
            elif start!= -1 and end!= -1:
                return word[start:end+1]
            start = -1
            end = -1
    if start!= -1 and end!= -1:
        return word[start:end+1]
    return

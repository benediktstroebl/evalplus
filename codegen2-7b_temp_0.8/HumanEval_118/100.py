
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
    if not word:
        return ""
    vowels = "aeiouAEIOU"
    index1 = len(word)-1
    while index1 >= 0:
        c = word[index1]
        if c in vowels:
            index2 = index1
            break
        index1 -= 1
    else:
        return ""
    index2 = index1
    while index2 >= 0:
        c = word[index2]
        if c in vowels:
            break
        index2 -= 1
    return word[max(index1, index2):index1+1] or word[index2:index1] or word[index1+1:index2] or word[index2+1:index

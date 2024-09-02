
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
    # ord('A') = 65, ord('z') = 122, ord('a') = 97, ord('Z') = 90
    vowels = ['A','E','I','O','U']
    vowels.extend(['a','e','i','o','u'])
    temp = word.rstrip('aeiouAEIOU')
    if(len(temp) <= 1):
        return ""
    i = len(temp) - 2
    while i > 0:
        if (temp[i] in vowels) and (temp[i-1] in vowels):
            return temp[i]
        i -= 1
    return ""


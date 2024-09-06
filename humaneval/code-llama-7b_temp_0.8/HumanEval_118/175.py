
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
    # TODO: Write your code here
    res = ''
    for i in range(len(word)-2, -1, -1):
        if word[i].isalpha() and word[i+1].isalpha() and word[i+2].isalpha():
            if word[i].islower():
                if word[i+1].isupper() or word[i+2].isupper():
                    res = word[i+1]
                    break
            elif word[i].isupper():
                if word[i+1].islower() or word[i+2].islower():
                    res = word[i+1]
                    break
    return res


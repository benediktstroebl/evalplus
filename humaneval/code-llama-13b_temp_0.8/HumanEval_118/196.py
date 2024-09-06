
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
    i = len(word)-1
    while i>0:
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u" or word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U":
            if word[i-1]!="a" and word[i-1]!="e" and word[i-1]!="i" and word[i-1]!="o" and word[i-1]!="u" and word[i-1]!="A" and word[i-1]!="E" and word[i-1]!="I" and word[i-1]!="O" and word[i-1]!="U":
                return word[i]
        i -= 1
    return ""
    

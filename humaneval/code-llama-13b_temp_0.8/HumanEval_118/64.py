
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
    vowel = ["a","e","i","o","u"]
    consonant = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    v_dict = {0:"a",1:"e",2:"i",3:"o",4:"u"}
    word = word.lower()
    if word[0] in vowel or word[-1] in vowel:
        return ""
    else:
        last_vowel = ""
        for i in range(len(word)-2,-1,-1):
            if word[i] in vowel:
                if word[i+1] in consonant and last_vowel == "":
                    last_vowel = word[i]
                else:
                    continue
            else:
                continue
        return last_vowel
        
        
    return ""


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
    vowels = 'aeiou'
    result = ""
    for i in range(len(word)):
        if word[i] in vowels:
            if i == 0:
                pass
            elif word[i-1] not in vowels:
                result = word[i-1:]
                break
            elif word[i-1] == word[i] and word[i-1] in vowels:
                pass
            elif word[i+1] not in vowels:
                result = word[i-1:]
                break
            elif word[i] == word[i-1] and word[i] == word[i+1]:
                pass
    return result


"""
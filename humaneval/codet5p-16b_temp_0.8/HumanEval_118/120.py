
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

    def get_vowels(word):
        vowels = set("aeiou")
        return list(filter(lambda x: x in vowels, word))

    for i in range(1, len(word)):
        if word[-i] not in "bcdfghjklmnpqrstvwxyz":
            continue
        if word[-i-1] not in "bcdfghjklmnpqrstvwxyz":
            return ""
        else:
            vowels = get_vowels(word[-i:])
            if vowels:
                return vowels[0]
    return ""

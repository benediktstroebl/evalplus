
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
        return None
    vowels = "aeiou"
    last_vowel = -1
    for i, c in enumerate(reversed(word)):
        if c in vowels:
            last_vowel = i
            break
    if last_vowel == -1:
        return ""
    front = word[:last_vowel]
    back = word[last_vowel:]
    # print(front, back)
    if len(front) == 0:
        return front
    for i in "aeiou":
        zz = front[-1]
        if i == zz:
            continue
        if last_vowel - 1 >= 0 and word[last_vowel - 1] in vowels and i in vowels:
            return i + back
    return ""

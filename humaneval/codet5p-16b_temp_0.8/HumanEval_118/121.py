
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

    cons = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] not in vowels:
            cons.append(word[i])
        else:
            break
    if cons == []:
        return ''
    for i in range(len(cons)):
        if cons[i] == vowels[0]:
            return vowels[0]
        if cons[i] == vowels[-1]:
            return vowels[-1]
    
    for i in vowels:
        if i in cons:
            return i
    return ''

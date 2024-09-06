
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
    word = word[::-1]
    l = []
    for i in range(len(word)):
        if word[i] in ['A', 'E', 'I', 'O', 'U']:
            l.append(i)

    l.append(len(word))
    if len(l) < 2:
        return ''
    else:
        for i in range(len(l)-1, -1, -1):
            if l[i] - l[i-1] > 1:
                return word[l[i-1]]

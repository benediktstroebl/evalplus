
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
    word = list(word)
    x = 0
    for i in range(len(word) - 1):
        if word[i] in 'aeiou' and word[i + 1] not in 'aeiou' and word[i - 1] not in 'aeiou':
            return word[i]
        if word[i] not in 'aeiou' and word[i + 1] in 'aeiou' and word[i - 1] not in 'aeiou':
            x = i
    if x == 0:
        return ""
    else:
        return word[x]
    print(get_closest_vowel('zoe'))
    print(get_closest_vowel('vowel'))
    print(get_closest_vowel('zoe zoe'))
    print(get_closest_vowel('zoe, zoe'))
    print(get_closest_vowel('zoe ,zoe'))
    print(get_closest_vowel('zoe,zoe

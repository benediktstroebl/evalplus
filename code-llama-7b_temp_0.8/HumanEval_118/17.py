
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
    index = -1
    vowel = ''
    # print(word)
    for i,l in enumerate(word[::-1]):
        # print(l)
        if l.lower() in 'aeiou':
            vowel = l
            # print(vowel)
            if i > 0 and word[len(word)-i-1].lower() in 'aeiou':
                return ''
            index = len(word)-i-1
            break
    if index == -1:
        return ''
    return vowel



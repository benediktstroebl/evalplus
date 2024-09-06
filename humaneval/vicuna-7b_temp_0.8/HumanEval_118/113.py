
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
    word = word.lower()
    start = 0
    end = 1
    while end <= len(word) and word[end] in 'bcdfghjklmnpqrstvwxyz':
        end += 1
    if end - start == 1:
        vowels = 'aeiou'
        for i in range(0, len(vowels) - 1):
            vowel = vowels[i]
            for j in range(start, end):
                if word[j] == vowel:
                    return vowel
            if word[start] == vowel:
                return vowel
        return ''
    else:
        return ''
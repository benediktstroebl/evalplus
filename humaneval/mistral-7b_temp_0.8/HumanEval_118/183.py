
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
    if word == '':
        return ''
    if 'y' in word or 'Y' in word:
        return ''
    if word[0] == word[-1]:
        return ''
    word_lower = word.lower()
    if word_lower[-1] == word_lower[0]:
        return ''
    if word_lower[-1] == 'y' or word_lower[-1] == 'Y':
        return ''
    for i in range(0, len(word_lower)):
        if word_lower[i] == 'a' or word_lower[i] == 'e' or word_lower[i] == 'i' or word_lower[i] == 'o' or word_lower[i] == 'u':
            if i >= 1 and word_lower[i-1] == 'y' or word_lower[i-1] == 'Y':
                if i < len(word_lower)-1 and word_lower[i+1] == 'y' or word_lower[i+1] == 'Y':
                    return word_lower[i

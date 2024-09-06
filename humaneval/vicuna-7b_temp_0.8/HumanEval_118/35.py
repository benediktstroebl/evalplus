
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
    index = 0
    previous_char = ''
    for i in range(len(word) - 1):
        if word[i] == word[i + 1] and word[i] in 'aeiouAEIOU':
            index = i
            previous_char = word[i - 1]
        elif word[i] != word[i + 1] and word[i] in 'aeiouAEIOU':
            index = i
            break
    return previous_char if index == 0 else ''

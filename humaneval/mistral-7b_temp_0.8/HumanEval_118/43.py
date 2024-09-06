
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
    # Write your code here
    words = word.split('')
    length = len(words)
    for i in range(length):
        if words[i] in 'AEIOUaeiou':
            if words[i - 1].isalpha() and words[i + 1].isalpha() and (words[i - 1].isupper() == words[i + 1].isupper()):
                return words[i]
    return ''

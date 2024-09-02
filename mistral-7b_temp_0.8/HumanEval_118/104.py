
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
    # Your code goes here
    word = word.lower()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    for i in word:
        if i not in vowels:
            if i in consonants:
                if len(word) == 1:
                    return ''
                elif i == word[-1]:
                    return ''
                elif i == word[0]:
                    return ''
                elif i == word[1]:
                    return ''
                elif word.find(i, word.find(i) + 1) == -1:
                    return ''
                else:
                    return word[word.find(i, word.find(i) + 1) - 1]
    else:
        return ''

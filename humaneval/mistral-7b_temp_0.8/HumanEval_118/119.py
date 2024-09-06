
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
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    # your code goes here
    last_vowel = word[-1]
    if last_vowel in vowels:
        return ''

    last_consonant = word[-2]
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels:
            continue
        elif word[i] in vowels and word[i + 1] in vowels:
            return ''
        elif word[i] in vowels and word[i + 1] not in vowels and word[i - 1] not in vowels:
            return word[i]
        elif word[i] in vowels and word[i + 1] not in vowels and word[i - 1] in vowels:
            return word[i - 1]
        elif word[i] not in vowels and word[i + 1] in v


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
    vowels = set(string.ascii_letters) - set(string.punctuation)
    vowels_count = {}
    for vowel in vowels:
        vowels_count[vowel] = vowels_count.get(vowel, 0) + 1
    word_len = len(word)
    for i in range(1, word_len):
        consonants = [word[:i], word[i+1:]]
        if len(consonants) == 1:
            continue
        if all(c.isalpha() for c in consonants):
            vowel_index = vowels_count[min(vowels, key=vowels_count.get)]
            if vowel_index != 0:
                return vowels[vowel_index-1]
    return ""
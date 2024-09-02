
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    def is_consonant(letter):
        return letter.isalpha() and letter not in vowels
    def get_consonant_index(word):
        return len(word) - word[::-1].find(word[-1]) - 1

    if len(word) < 3:
        return ''
    if is_consonant(word[0]) and is_consonant(word[1]):
        index_1 = get_consonant_index(word)
        if index_1 == -1:
            return ''
        return word[index_1 - 1]
    for index in range(len(word) - 2, -1, -1):
        if is_consonant(word[index]) and is_consonant(word[index + 1]):
            return word[index + 1]
    return ''

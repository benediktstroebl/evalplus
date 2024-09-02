
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_indices = [i for i, x in enumerate(word) if x in vowels]
    if len(vowels_indices) < 2:
        return ''
    else:
        vowels_indices.reverse()
        indices = range(len(vowels_indices))
        indices = list(map(lambda x: x - 1, indices))
        for i, v in zip(vowels_indices, indices):
            if v != -1 and i != 0:
                return word[i]
        return ''

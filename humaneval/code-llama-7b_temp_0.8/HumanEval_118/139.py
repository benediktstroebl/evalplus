
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
    # find vowels
    vowels = [i for i in word if i in 'aeiou']
    # filter consonants
    consonants = [i for i in word if i not in 'aeiouAEIOU']
    if len(consonants) <= 0:
        return ''
    # get closest vowel
    closest_vowel = ''
    for i, c in enumerate(consonants):
        if i < len(consonants) - 1:
            next_consonant_idx = i + 1
            # find the next closest vowel from the next consonant
            next_closest_vowel = [i for i in vowels if i > consonants[next_consonant_idx]]
            if len(next_closest_vowel) > 0:
                closest_vowel = min(next_closest_vowel)
                return closest_vowel
        else:
            # the last consonant
            closest_vowel = vowels[-1]
            return closest_vowel




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
    if len(word) < 3:
        return ''

    found_vowel = ''
    i = len(word) - 2
    while i >= 0:
        if word[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] and \
           word[i+1] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            found_vowel = word[i]
            break
        i -= 1
    return found_vowel

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
        found_vowel = ''
        vowels = 'aeiouAEIOU'
        for i in range(len(word)-2, -1, -1):
            if word[i] in vowels and word[i+1] not in vowels:
                found_vowel = word[i]
                break
        return found_vowel

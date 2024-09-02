
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
    # your code here
    # 1. find first vowel
    # 2. check its previous char is consonant
    # 3. check its next char is consonant
    # 4. if both 2 and 3 true return vowel
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for v in vowels:
        if v in word[1:]:
            if word[word.index(v)-1].lower() in 'bcdfghjklmnpqrstvwxyz':
                if word[word.index(v)+1].lower() in 'bcdfghjklmnpqrstvwxyz':
                    return v
    return ''



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
    letters = list(word)
    consonants = [
        i for i in range(len(letters)-2)
        if letters[i] not in "aeiouAEIOU"
    ]
    vowel_i = [i for i in consonants if letters[i] in "aeiouAEIOU"]
    if not vowel_i:
        return ""
    return min(
        (vowels - set(letters[i] for i in vowel_i), i)
        for i in vowel_i[1:]
        for vowels in (
            set(letters[i] for i in vowel_i) | set(letters[vowel_i[0]]),
            set(letters[vowel_i[-1]]),
            set(letters[i] for i in range(vowel_i[0]-1, -1, -1) if letters[i] in "aeiouAEIOU"),
        )
    )[1]


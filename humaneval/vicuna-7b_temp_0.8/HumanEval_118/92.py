
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
    vowels = set(string.ascii_letters) - {'a', 'e', 'i', 'o', 'u'}
    n = len(word)
    for i in range(n-1):
        for j in range(i+1, n):
            if word[i] in vowels and word[j] in vowels and word[i] < word[j]:
                return word[i]
        if word[i] in vowels:
            return word[i]
    return ""

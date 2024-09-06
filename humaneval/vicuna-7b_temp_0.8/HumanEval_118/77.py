
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

    if len(word) < 2 or len(word) > 4:
        return ""
    vowels = "aeiouAEIOU"
    start = 0
    end = len(word) - 1
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i+1] in vowels:
            if len(word[start:i]) == 1:
                start = i
            if len(word[i+1:end]) == 1:
                end = i
            if start < end:
                if len(word[start:end]) > 1:
                    return word[start:end]
                break
        end = i - 1
    return ""

word = input("Enter a word: ")
closest_vowel = get_closest_vowel(word)

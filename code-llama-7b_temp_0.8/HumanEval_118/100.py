
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
    # My and best solutions
    def closest_vowel_1(word):
        vowels = "AEIOUaeiou"
        for i in range(len(word)-1, -1, -1):
            if word[i] in vowels and word[i+1] in vowels:
                return word[i]
        return ""

    def closest_vowel_2(word):
        vowels = "AEIOUaeiou"
        for i in range(len(word)-1, -1, -1):
            if word[i] in vowels and word[i+1] in vowels:
                return word[i+1]
        return ""

    # Best practice
    def closest_vowel_3(word):
        vowels = "AEIOUaeiou"
        return next((word[i+1] for i in range(len(word)-1, -1, -1) if word[i] in vowels and word[i+1] in vowels), "")

    # Other practice
    def closest_vowel_4(word):
        vowels = "AEIOUaeiou"
        for i in range(len(word)-2, -1, -1):
            if word[i] in vowels and word[i+1] in vowels:
                return word[i+1]
        return ""
    
    return closest_vowel_4(word)


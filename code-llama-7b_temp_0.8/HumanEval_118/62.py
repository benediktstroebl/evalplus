
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
    # Rules: 
    # 1. if the word starts with a vowel, return empty string
    # 2. if the word ends with a vowel, return empty string
    # 3. if the word has one vowel, return empty string
    # 4. if the word has two vowels, return the first one
    # 5. if the word has three vowels, return the first one
    # 6. else, find the vowel between the first and second consonant from the right
    
    # Step 1
    if word[0] in "aeiou":
        return ""
    if word[-1] in "aeiou":
        return ""
    if word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") == 1:
        return ""
    if word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") == 2:
        return word[1]
    
    # Step 2
    for i in range(1, len(word)-1):
        if word[i] in "aeiou":
            return word[i]
    return ""



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
    # Using a list to store vowels
    vowels = "aeiouAEIOU"
    # Iterating through the word
    for i in range(len(word)):
        if word[i] == "R":
            continue
        if word[i] == "N":
            continue
        if word[i] == "S":
            continue
        if word[i] == "T":
            continue
        # Iterating through the word again
        for j in range(i+1, len(word)):
            # Check if the vowel is between the consonants
            if word[i] == word[j] and word[i] in vowels:
                return word[i]
            elif word[i] == word[j] and word[j] in vowels:
                return word[j]
        return ""

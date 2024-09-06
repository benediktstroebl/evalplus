
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
    # RULES:
    # 1. The closest vowel is in between two consonants.
    # 2. Vowels at the beginning or ending of a word are excluded.
    # 3. If there is no vowel between two consonants, return ""
    # 4. All letters in the given string are in capital letters.

    # edge cases
    # ""
    # "A"
    # "Aa"
    # "Aaa"
    # "AaAa"
    # "AaAaA"
    # "AaAaAa"

    # base cases
    # "AaaaA"
    # "AaaAaaA"
    # "AaaAaaAaa"

    # general cases
    # "AaAaaA"
    # "AaAaaAa"

    vowels = "AEIOU"

    # 1. check if there are two consonants in the word
    for i in range(len(word)-1):
        if word[i] not in vowels and word[i+1] not in vowels:
            return word[i+1]
    return ""


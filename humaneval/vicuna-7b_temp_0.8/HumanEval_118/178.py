
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
    if len(word) < 2 or word == "":
        return ""
    for i in range(len(word)-1, -1, -1):
        for j in range(i+1, len(word)):
            if word[i] == "w" or word[i] == "h" or word[i] == "y" and word[j] == "e" or\
               word[j] == "a" or word[j] == "o" or word[j] == "u":
                if abs(word[i] - word[j]) < abs(word[i] - word[i+1]):
                    return word[i]
    return ""

word = input("Enter the word: ")
closest_vowel = get_closest_vowel(word)

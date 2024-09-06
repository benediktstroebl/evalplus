
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
    # convert the string to lowercase and split into words
    word = word.lower()
    words = word.split()

    # check if the word is empty
    if not words:
        return ""

    # initialize the closest vowel and its distance
    closest_vowel = ""
    closest_distance = float("inf")

    # check the first word
    if words[0].lower() == "a" or words[0].lower() == "e" or words[0].lower() == "i" or words[0].lower() == "o" or words[0].lower() == "u":
        # check the closest vowel between two consonants
        for i in range(1, len(words)):
            for j in range(i):
                if words[j].lower() == "b" or words[j].lower() == "c" or words[j].lower() == "d" or words[j].lower() == "f" or words[j].lower() == "g" or words[j].lower() == "h" or

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
    length = len(word)
    vowels = set("aeiouAEIOU")
    count = 0
    for i in range(0, length):
        for j in range(i+1, length):
            if word[i] == word[j] and word[i].isalpha() and word[j].isalpha():
                if word[i].lower() in vowels and word[j].lower() not in vowels:
                    count += 1
                    if count == 2:
                        return word[i].lower()
    return ""

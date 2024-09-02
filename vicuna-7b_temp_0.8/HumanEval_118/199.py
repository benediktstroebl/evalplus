
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
    left_index = word.find("c")
    right_index = len(word) - 1

    vowel = ""
    if left_index == -1 or right_index == -1:
        return ""
    for i in range(left_index, right_index + 1):
        if word[i] == "c" or word[i] == "s":
            continue
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            distance = abs(left_index - i)
            if distance < len(word) - 1:
                if word[i - 1] != "a" and word[i - 1] != "e" and word[i - 1] != "i" and word[i - 1] != "o" and word[i - 1] != "u":
                    vowel = word[i]
                    break
            if distance > 1:
                vowel = word[i]
                break
    return vowel
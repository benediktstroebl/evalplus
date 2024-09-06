
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
    result = ""
    start = 0
    end = 0
    while end < len(word):
        if word[end] == "r":
            end += 1
        elif word[end] == "n":
            end += 1
        elif word[end] == "s":
            end += 1
        elif word[end] == "t":
            end += 1
        elif word[end] == "l":
            end += 1
        else:
            start = end
            while word[start] == "c" or word[start] == "s" or word[start] == "h" or word[start] == "x":
                start += 1
            if word[start] == "e" or word[start] == "i" or word[start] == "u":
                result = word[start]
                end = start - 1
                break
            elif word[start] == "y":
                while word[start + 1] != "u":
                    start += 1
                if word[start] == "e" or word[start] == "i" or word[start] == "u":
                    result = word[start]
                    end = start - 1
                    break
                else:
                    result = ""
            else:
                result = ""
    return result

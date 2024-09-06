
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
    # your code here
    for i in range(len(word)):
        if (i == 0 and word[0].isalpha()) or (i == len(word) - 1 and word[len(word)-1].isalpha()):
            continue
        elif word[i].isalpha() and word[i-1].isalpha() and word[i+1].isalpha():
            if word[i].isalpha():
                if word[i-1].lower() in "aeiou" and word[i+1].lower() in "aeiou":
                    return word[i]
                elif word[i-1].lower() in "aeiou" and not word[i+1].isalpha():
                    return word[i]
                elif word[i+1].lower() in "aeiou" and not word[i-1].isalpha():
                    return word[i]
    return ''




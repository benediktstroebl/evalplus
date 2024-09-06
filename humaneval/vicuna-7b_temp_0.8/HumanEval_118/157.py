
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
    result = ''
    index = 0
    while index < len(word) - 1:
        if not word[index].isalpha():
            # check if word[index] is a vowel
            if word[index] == 'a' or word[index] == 'e' or word[index] == 'i' or word[index] == 'o' or word[index] == 'u':
                # check if the closest vowel is between two consonants from the right side
                for i in range(index, len(word) - 1):
                    if not word[i].isalpha() or word[i] == ' ':
                        closest_vowel = word[index:i]
                        break
                    i += 1
                if closest_vowel:
                    result = closest_vowel[0]
                    break
    return result or ''

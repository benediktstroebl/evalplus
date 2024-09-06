
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
    if not word:
        return ""
    word = list(word)
    start_index = 0
    end_index = len(word) - 1
    while start_index < end_index:
        if word[start_index].isalpha() and not word[start_index].isupper() and word[start_index].lower() not in "aeiou":
            start_index += 1
        elif word[end_index].isalpha() and not word[end_index].isupper() and word[end_index].lower() not in "aeiou":
            end_index -= 1
        elif word[start_index].isalpha() and not word[start_index].isupper() and word[start_index].lower() in "aeiou" and \
                word[end_index].isalpha() and not word[end_index].isupper() and word[end_index].lower() in "aeiou":
            return word[start_index + 1 : end_index].lower().strip()
        elif word[start_index].isalpha() and not word

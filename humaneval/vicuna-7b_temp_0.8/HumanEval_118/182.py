
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
    vowel_count = 0
    start = 0
    end = 0
    current_word = word
    while True:
        start = end + 1
        end = start + 1
        for i in range(start, len(current_word)):
            if current_word[i] == 'r' or current_word[i] == 'n':
                break
            elif current_word[i] == 'l' or current_word[i] == 'p':
                end = i - 1
            elif current_word[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
            else:
                vowel_count -= 1
                if vowel_count == 0:
                    return current_word[start:end]
                if vowel_count < 0:
                    return ""
        start += 1
        current_word = current_word[start:]


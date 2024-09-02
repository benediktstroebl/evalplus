
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
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = word[::-1]
    index = 0
    vowel_index = 0
    vowel = ""

    for i in new_word:
        if i in vowels:
            vowel = i
            vowel_index = index
            break
        index += 1

    if vowel_index > 0:
        return vowel
    else:
        return ""


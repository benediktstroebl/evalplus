
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
    vowel_index = [i for i, char in enumerate(word) if char in 'aeiouAEIOU']
    if not vowel_index:
        return ''
    if len(vowel_index) > 1:
        max_index = max(vowel_index)
        next_index = vowel_index[max_index]
    else:
        max_index = 0
        next_index = vowel_index[max_index]
    if len(word) > max_index+1:
        next_letter = word[max_index+1]
        if next_letter == ' ':
            max_index += 1
        if next_letter == word[0]:
            return ''
    return word[max_index+1]

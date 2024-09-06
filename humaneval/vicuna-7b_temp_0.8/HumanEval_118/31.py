
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
    vowels = "aeiouAEIOU"
    previous_cons = ''
    current_cons = ''
    vowel_found = False
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels and word[i] != word[i + 1]:
            if not vowel_found and vowels.index(word[i]) == vowels.index(word[i + 1]):
                vowel_found = True
                current_cons = word[i]
            elif vowel_found and vowels.index(word[i + 1]) == vowels.index(word[i]):
                vowel_found = True
                current_cons = word[i + 1]
            if current_cons != previous_cons:
                if vowel_found:
                    return current_cons
                vowel_found = False
                previous_cons = current_cons
    if vowel_found:
        return current_cons
    return ''

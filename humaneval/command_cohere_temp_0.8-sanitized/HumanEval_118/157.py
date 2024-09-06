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
    # Use a dictionary to check if next char to right is a consonant
    word = word.lower()
    char_dict = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1
        }
    vowel_index = -1
    for i in range(len(word)-1):
        if word[i] in char_dict:
            if char_dict[word[i]] == 1:
                vowel_index = i
        char_dict[word[i+1]] = 1
    if vowel_index != -1:
        return word[vowel_index]
    else:
        return ""
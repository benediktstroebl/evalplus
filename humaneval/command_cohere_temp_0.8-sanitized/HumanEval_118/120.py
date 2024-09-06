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
    # Use a dictionary to check if current char is vowel or consonant
    # Initialize anchor as None
    vowel_dict = {'y': 'Y', 'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
    anchor = None
    output = ''
    for char in word:
        if char in vowel_dict.values() and anchor is not None:
            if vowel_dict[char] != anchor:
                output += char
                anchor = vowel_dict[char]
        elif char in vowel_dict.values():
            anchor = vowel_dict[char]
        elif anchor is not None:
            pass
        else:
            continue
    return output
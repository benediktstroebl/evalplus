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
    # use a pointer to scan the right most end of the word
    pointer = len(word) - 1
    result = ""
    
    # iterate through the word characters
    for char in word:
        # Check if current char is a vowel
        if char.lower() in 'aeiou':
            # If the pointer points to a consonant, update the result
            if pointer > 0 and word[pointer - 1].lower() not in 'aeiou':
                result = char
            # Move the pointer one step back to find the next closest vowel
            pointer -= 1
        else:
            pointer = len(word) - 1
    
    return result
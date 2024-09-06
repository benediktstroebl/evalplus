
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
    # Split string to list
    word = list(word)
    # Reverse order
    word.reverse()
    # Make new list to store indexes
    index = []
    # Find vowels
    for i, v in enumerate(word):
        if v in "aeiou":
            index.append(i)
    # If there is no vowels, return empty string
    if not index:
        return ""
    # Find the closest vowel
    if len(index) >= 2:
        if index[1] - index[0] <= 1:
            return word[index[0]]
        else:
            return word[index[1]]
    elif len(index) == 1:
        if index[0] == 0:
            return ""
        if index[0] == 1:
            if word[1] in "aeiou":
                return word[1]
            else:
                return word[0]
    else:
        return ""



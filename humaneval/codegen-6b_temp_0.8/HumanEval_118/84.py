
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
    # use stacks to store front and back
    # find closest to the front
    # use counter to store the number of consonants
    # search from the end of the word to the front
    # for each character, compare to the counter
    # if counter > 0, then append to front
    # if counter < 0, pop the front and compare to counter
    # if counter = 0, then pop the front and pop the back
    # return the front
    front = []
    back = []
    vowels = "aeiou"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            front.append(word[i])
        if word[i] not in vowels:
            back.append(word[i])
        if len(front) > 0 and len(back) > 0:
            if abs(len(back)-len(front)) >= 2:
                return front.pop()
            if abs(len(back)-len(front)) == 1:
                return back.pop()
    return ""

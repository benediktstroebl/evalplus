
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
    if word[0] == "y" or word[0] == "Y":
        return ""
    vowels = ["a", "e", "i", "o", "u"]
    first = word[0]
    pos = 1
    cons = list()
    last = word[-1]
    while pos < len(word) - 1:
        if first.isupper():
            first = word[pos]
            pos += 1
        elif word[pos].isupper():
            if first != word[pos]:
                cons.append(word[pos])
            first = word[pos]
            pos += 1
    cons.append(last)
    ans = list()
    for c in cons:
        if c.lower() in vowels:
            return c
        ans.append(c)
    return "".join(ans)

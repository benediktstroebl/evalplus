
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
    # initialize dp as empty list
    dp = []
    # initialize gap as 1
    gap = 1
    # check if the word is empty
    if not word:
        return ""
    # check if the word contains only one letter
    if len(word) == 1:
        return word
    # iterate through the word
    for i in range(len(word)):
        # check if the word contains a single consonant
        if len(word) - i == 1:
            # if yes then check if the next consonant is same as the current consonant and if yes then add 2 to gap
            if word[i] == word[i+1]:
                gap = gap + 2
        # if not then check if the consonant is a vowel
        else:
            for j in range(i, len(word)):
                # check if the word contains a single vowel
                if len(word) - j == 1:
                    # if yes then check if the current consonant is same as the previous vowel and if yes then add 1 to gap
                    if word[i] == word[j-1]:
                        gap = gap + 1
                # if not then check if the vowel is the closest
                else:
                    # if yes then add the gap + 1 to dp
                    dp.append(gap + 1)
    # return the closest vowel
    return "".join([word[i] for i in dp[d
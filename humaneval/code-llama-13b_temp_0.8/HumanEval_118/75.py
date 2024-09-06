
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
    vowels = "aeiouAEIOU"
    vowels_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowels_list.append(word[i])
    answer = []
    for i in range(len(word)-1,0,-1):
        if word[i] in vowels and word[i-1] not in vowels:
            answer.append(word[i])
        if word[i] not in vowels and word[i-1] in vowels:
            answer.append(word[i-1])
    if len(answer) == 0:
        return ""
    else:
        return answer[0]


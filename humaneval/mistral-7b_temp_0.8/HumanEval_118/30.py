
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
    # Write your code here.
    answer = ""
    temp = ""
    for i in range(len(word)):
        if(word[i].islower() or word[i].isupper()):
            if(word[i] in "aeiouAEIOU"):
                answer = word[i]
        elif(word[i] == " "):
            continue
        else:
            temp += word[i]

    if(len(temp) % 2 == 1):
        for i in range(len(temp)):
            if(temp[i] in "aeiouAEIOU"):
                answer = temp[i]

    return answer


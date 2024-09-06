
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
    if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
        return ""
    
    vowels =['a','e','i','o','u']
    output = ""
    
    #1.Get all possible combinations of consonants
    
    con_lst = []
    for i in range(0, len(word)-1):
        if word[i] not in vowels and word[i+1] not in vowels:
            con_lst.append(word[i]+word[i+1])
    
    #2.Get the closest one
    
    final_output = ""
    
    for con in con_lst:
        if len(con) > len(output):
            final_output = con
    
    if final_output == "":
        return ""
    
    return final_output

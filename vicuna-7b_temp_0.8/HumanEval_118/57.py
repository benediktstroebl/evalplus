
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
    # set empty list to store closest vowel
    closest_vowel = []
    # split the word by space
    words = word.split(" ")
    for word in words:
        if word == "":
            continue
        if word[0] == word[-1] and word[-1] == "c":
            # check if the word starts with "cc"
            if len(word) == 2:
                continue
            # check if the word starts with "cv"
            if word.find("v") != -1:
                # get the index of vowel
                vowel_index = word.find("v")
                # check if the vowel is present in the word
                if vowel_index != -1:
                    # append the index of vowel to the list
                    closest_vowel.append(vowel_index)
    if len(closest_vowel) == 0:
        return ""
    else:
        # remove the duplicates
        closest_vowel = closest_vowel[:-1]
        # return the closest vowel
        return "".join([word[i:i+1] for i in closest_vowel if i != -1])

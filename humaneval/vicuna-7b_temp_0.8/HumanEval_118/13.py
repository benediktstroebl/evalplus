
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
    # remove all non-alphanumeric characters from the word
    word = ''.join([c for c in word if c.isalnum()])
    
    # split the word into a list of characters
    words = word.split('')
    
    # initialize variables to store the starting and ending indices of the closest vowel
    start_index = 0
    end_index = 0
    
    # iterate through each character in the word
    for i in range(len(words)):
        # check if the current character is a consonant
        if words[i].isupper() or words[i].islower():
            # check if the next character is a vowel
            if i < len(words) - 1:
                if words[i+1].isupper() or words[i+1].islower():
                    # find the index of the vowel between the two consonants
                    for j in range(i+1, len(words)):
                        if words[j].isupper() or words[j].islower():
                            break
                    start_index = i + 1
                    end_index = j
                    break
            else:
                end_index = i
                break
    
    # return the closest vowel or an empty string if none is found
    if start_index == end_index:
        return ''
    else:
        return words[start_index]

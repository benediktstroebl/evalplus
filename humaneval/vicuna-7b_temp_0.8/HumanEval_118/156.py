
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
    words = word.lower().split()
    vowel = ""
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == "r" and words[j] == "n":
                if words[i+1] == "t" or words[j-1] == "t":
                    continue
                elif words[i+1] == "l" or words[j-1] == "l":
                    continue
                elif words[i+1] == "s" or words[j-1] == "s":
                    continue
                elif words[i+1] == "v" or words[j-1] == "v":
                    continue
                elif words[i] == "a" and words[j] == "e":
                    continue
                elif words[i] == "i" and words[j] == "i":
                    continue
                elif words[i] == "u" and words[j] == "u":
                    continue
                elif words[i] == "o" and words[j] == "o":
                    continue
                elif words[i] == "y" and words[j] == "w":
                    continue
                elif words[i] == "h" and words[j] == "w":
                    continue
                elif words[i] == "m" and words[j] == "n":
                    continue
                elif words[i] == "n" and words[j] == "n":
                    continue
                elif words[i] == "p" and words[j] == "p":
                    continue
                elif words[i] == "b" and words[j] == "v":
                    continue
                elif words[i] == "d" and words[j] == "d":
                    continue
                elif words[i] == "g" and words[j] == "g":
                    continue
                elif words[i] == "c" and words[j] == "c":
                    continue
                elif words[i] == "f" and words[j] == "f":
                    continue
                else

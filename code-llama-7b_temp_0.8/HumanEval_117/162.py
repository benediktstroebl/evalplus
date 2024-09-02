
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    #define our variables
    words = []
    consonants = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    #turn s into a list
    s = s.split(" ")
    #for each word in s
    for i in range(len(s)):
        #if the length of the word is == n
        if len(s[i]) == n:
            #loop through each letter in the word
            for j in range(len(s[i])):
                #check if the letter is not a consonant
                if s[i][j] not in consonants:
                    #if it's not a consonant, break
                    break
            #if the loop was broken, the word has n consonants
            else:
                #append it to words
                words.append(s[i])
    #return words
    return words

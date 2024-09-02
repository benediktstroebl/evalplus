
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

    #check that string s is not empty
    if s == '':
        return []
    else:
        #initalize list to store words
        words_list = []
        #split string into list
        s_list = s.split()
        #loop through list to check number of consonants
        for word in s_list:
            #count the number of consonants
            vowels = 'aeiou'
            consonants_count = 0
            for char in word:
                if char not in vowels:
                    consonants_count += 1

            #check that the number of consonants in string is equal to n
            if consonants_count == n:
                words_list.append(word)

        return words_list

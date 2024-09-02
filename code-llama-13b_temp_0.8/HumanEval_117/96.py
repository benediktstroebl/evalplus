
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
    # Planning:
    # 1. define a function that takes 2 arguments, the string and the natural number
    # 2. find all the vowels in the string
    # 3. find all the consonants in the string
    # 4. return a list of words in the string with exactly n consonants
    
    # def 
    
    # vowels = 'aeiou'
    # consonants = ''
    # for letters in s:
    #     if letters not in vowels:
    #         consonants += letters
    # print(consonants)


    # consonant_letters = [letters for letters in s if letters not in 'aeiou']
    # print(consonant_letters)
    # if len(consonant_letters) == n:
    #     print(s)

    

    # word_list = []
    # for words in s.split():
    #     if len(words) == n:
    #         word_list.append(words)
    # return word_list




    # return a list of words in the string with exactly n consonants
    pass


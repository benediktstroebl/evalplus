
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
    # Your code here

    # Solution 1
    # words = s.split()
    # final_list = []
    # for word in words:
    #     vowels = 'aeiou'
    #     if len(word) == n:
    #         counter = 0
    #         for letter in word:
    #             if letter not in vowels:
    #                 counter += 1
    #         if counter == n:
    #             final_list.append(word)
    # return final_list

    # Solution 2
    vowels = 'aeiou'
    return list(word for word in s.split() if len(word) == n and all(letter not in vowels for letter in word))

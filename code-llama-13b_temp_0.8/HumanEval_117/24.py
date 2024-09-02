
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
    # def select_words(s, n):
    #     # your code here
    #     if len(s) == 0:
    #         return []
        
    #     res = []
    #     word_counter = 0
    #     str_arr = s.split(" ")
    #     for i in range(len(str_arr)):
    #         # check for first letter to be alphabet
    #         if str_arr[i][0].isalpha():
    #             # counter for consonant
    #             consonant_counter = 0
    #             for j in range(len(str_arr[i])):
    #                 # check for alphabet
    #                 if str_arr[i][j].isalpha():
    #                     # check for consonant
    #                     if not str_arr[i][j].lower() in ['a', 'e', 'i', 'o', 'u']:
    #                         consonant_counter += 1
    #             # check if number of consonant is equal to n
    #             if consonant_counter == n:
    #                 res.append(str_arr[i])

    #     return res

    #     """
    #     # time O(n)
    #     # space O(n)
    #     """
    
    def select_words(s, n):
        """
        # time O(n)
        # space O(n)
        """
        result = []

        for word in s.split():
            consonants = sum(1 for c in word if c not in 'aeiouAEIOU')
            if consonants == n:
                result.append(word)
        return result

    return select_words(s, n)

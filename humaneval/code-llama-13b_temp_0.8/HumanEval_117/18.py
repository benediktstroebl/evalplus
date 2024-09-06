
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
    # if s == '':
    #     return []
    # arr = []
    # count = 0
    # i = 0
    # while i < len(s):
    #     if s[i] != ' ' and s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u':
    #         count += 1
    #     else:
    #         count = 0
    #     if count == n:
    #         string = s[i]
    #         while i < len(s) - 1:
    #             if s[i+1] != ' ':
    #                 string += s[i+1]
    #                 i += 1
    #             else:
    #                 break
    #         arr.append(string)
    #         count = 0
    #     i += 1
    # return arr
    if s == '':
        return []
    words = s.split()
    ans = []
    vowels = 'aeiouAEIOU'
    for word in words:
        count = 0
        for letter in word:
            if letter not in vowels:
                count += 1
            if count == n:
                ans.append(word)
                break
    return ans

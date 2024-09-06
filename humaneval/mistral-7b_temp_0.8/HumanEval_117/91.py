
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
    result = []
    for i in range(len(s)):
        temp = ""
        j = i
        while j < len(s):
            if s[j] != " ":
                temp += s[j]
            else:
                if temp.count("a") + temp.count("e") + temp.count("i") + temp.count("o") + temp.count("u") + temp.count("y") == n:
                    result.append(temp)
                temp = ""
                j += 1
        if temp.count("a") + temp.count("e") + temp.count("i") + temp.count("o") + temp.count("u") + temp.count("y") == n:
            result.append(temp)

    return result

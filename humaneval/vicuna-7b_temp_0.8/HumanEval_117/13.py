
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
    # print(s)
    # print(n)
    # check if string is empty
    if not s:
        return []
    # check if string contains n consonants
    count = 0
    for char in s:
        if char.isalpha() and char.islower() and char.isnumeric() == False:
            count += 1
    if count == n:
        return [s]
    # check if the string contains n consonants in reverse order
    count = 0
    for char in s:
        if char.isalpha() and char.islower() and char.isnumeric() == False:
            count += 1
    if count == n:
        return [s]
    # check if the string contains only n consonants
    count = 0
    for char in s:
        if char.isalpha() and char.islower() and char.isnumeric() == False:
            count += 1
    if count == n:
        return [s]
    # check if the string contains n consonants in reverse order
    count = 0
    for char in s:
        if char.isalpha() and char.islower() and char.isnumeric() == False:
            count += 1
    if count == n:
        return [s]
    # print("count is : ", count)
    # print("n is : ", n)
    # print("char : ", s[0])
    # print("s is : ", s)
    return []

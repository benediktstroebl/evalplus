
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
    # Todo: implement function
    # ROT13
    letters = []
    for i in range(len(s)):
        if s[i].isalpha():
            letters.append(s[i])
    letters = "".join(letters)
    rot13 = ""
    for i in range(len(letters)):
        if letters[i].isupper():
            if ord(letters[i]) - 13 >= ord('A'):
                rot13 += chr(ord(letters[i]) - 13)
            else:
                rot13 += chr(ord('A') + 13 - ord(letters[i]))
        else:
            if ord(letters[i]) + 13 <= ord('z'):
                rot13 += chr(ord(letters[i]) + 13)
            else:
                rot13 += chr(ord('z') - 13 + ord(letters[i]))
    words = rot13.split()
    words = [word for word in words if len([char

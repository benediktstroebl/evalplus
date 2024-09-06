
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Create an empty list
    lst = []
    # Create a flag for checking if there are whitespaces in the text
    flag = 0
    # Create a flag for checking if there are commas in the text
    flag1 = 0
    # Create a flag for checking if there are lowercase letters with odd order in the alphabet
    flag2 = 0
    # Run a loop to check if there are whitespaces, commas or lowercase letters with odd order in the alphabet
    for i in txt:
        # If a whitespace is found, add it to the list
        if i == " ":
            lst.append(i)
            flag = 1
            flag1 = 0
            flag2 = 0
        # If a comma is found, add it to the list
        elif i == ",":
            lst.append(i)
            flag = 0
            flag1 = 1
            flag2 = 0
        # If a lowercase letter is found, check if it has odd order in the alphabet
        else:
            if 97 <= ord(i


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
    # Write your code here
    # Pseudocode
    # split words on whitespaces
    # split words on commas
    # split words on the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    # Return the output

    # Split words on whitespaces
    words = txt.split()
    print("Split words on whitespaces: ", words)

    # Split words on commas
    words = txt.split(",")
    print("Split words on commas: ", words)

    # Split words on lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    words = txt.split("abcdef")
    print("Split words on lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25: ", words)

    # Return the output

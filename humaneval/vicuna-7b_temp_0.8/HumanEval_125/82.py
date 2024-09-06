
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
    # Split the text on whitespace and replace whitespace with empty string
    txt = txt.split()
    txt = [txt.replace(" ", "") for txt in txt]
    # Get the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    letter_count = [ord(c) for c in txt] // 2
    # Get the length of the longest substring without repeating characters
    str_lengths = [len(txt[i:i + 1]) for i in range(len(txt) - 1)]
    # Return the list of words and the number of lower-case letters with odd order in the alphabet
    return txt[1:], [letter_count[i] for i in range(len(str_lengths)) if str_lengths[i] > 0]

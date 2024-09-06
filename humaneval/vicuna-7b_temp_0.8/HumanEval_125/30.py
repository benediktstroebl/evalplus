
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

    # split_words("Hello world!") ➞ ["Hello", "world!"]
    words = txt.split()
    # split_words("Hello,world!") ➞ ["Hello", "world!"]
    words = txt.split(',')
    # split_words("abcdef") ➞ 3
    words = [word for word in words if word.isalpha()]
    word_counts = {}
    for word in words:
        if len(word) % 2 == 1:
            # split_words("abcdef") ➞ 3
            word_counts[ord(word[0]) - ord('a')] = word_counts.get(ord(word[0]) - ord('a'), 0) + 1
    return list(word_counts.keys())


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
    txt = txt.strip()
    words = txt.split() if txt.strip().lower() == '' else txt.split(',')
    return words

if __name__ == '__main__':
    text = input("Enter text: ")
    print(split_words(text))
\end{code}

Comment: This solution only works if the string is a single word, and it will split the string on every whitespace character. It is also not correct for the example given in the problem statement.

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
    # return txt.split()
    # return txt.split(",")

    def countOddLetters(text):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        letters = []
        for letter in text:
            if letter in alphabets:
                letters.append(letter)

        letters_count = []
        for letter in letters:
            if ord(letter) % 2 == 1:
                letters_count.append(letter)
        return len(letters_count)

    return countOddLetters(txt)


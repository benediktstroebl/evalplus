
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
    # initialize a dictionary to count letters for each word
    word_count = Counter()
    # initialize an empty list to store the words
    words = []
    # initialize a string to store the current word
    current_word = ''
    # initialize a variable to store the position of the current character in the string
    current_position = 0
    # iterate through the string
    for i in range(len(txt)):
        # if the current character is a space or comma, add the word to the list and start a new word
        if txt[i] == ' ' or txt[i] == ',' or (i == 0 and txt[i] == ','):
            if current_word:
                words.append(current_word)
                current_word = ''
            # if the current character is not a space or comma, add the current character to the current word
            else:
                current_word += txt[i]
        # if the current word is not empty, add it to the word_count dictionary and the words list
            if current_word:
                word_count[current_word] += 1
                words.append(current_word)
                current_word = ''
        # if the current position is at the end of the string, increment the position and check if the word_count dictionary
            # contains a key with the length of the current word
                current_position += 1
                if current_position == len(txt):
                    word_str = ''.join([txt[i] for i in range(len(txt)) if txt[i] != ' '])
                    if word_str in word_count:
                        return word_count[word_str]
    # return 0 if the string is empty
    return 0
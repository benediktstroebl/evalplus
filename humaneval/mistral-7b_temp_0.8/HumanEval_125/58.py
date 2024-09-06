
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
    words = [x for x in txt]
    split_words = []
    counter = 0
    for x in range(len(words)):
        for y in range(len(words[x])):
            if words[x][y] == ',':
                split_words.append(words[x][:y])
                words.remove(words[x])
                words.append(words[x][y+1:])
                break
            if words[x][y] == ' ':
                split_words.append(words[x][:y])
                words.remove(words[x])
                words.append(words[x][y+1:])
                break
    #print(words)
    #print(split_words)
    for x in range(len(words)):
        if ord(words[x][0]) % 2 != 0:
            counter += 1
    return counter


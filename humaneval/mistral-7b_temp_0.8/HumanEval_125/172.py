
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
    #Implement your code here
    words = []
    for letter in txt:
        words.append(letter)
    if not words:
        return 0
    else:
        if words[0] == ' ' or words[0] == ',' or words[0] == '.':
            words.pop(0)
        if words[len(words) - 1] == ' ' or words[len(words) - 1] == ',' or words[len(words) - 1] == '.':
            words.pop(-1)
        new_list = []
        for i in words:
            if i == ' ' or i == ',' or i == '.':
                new_list.append(i)
        words = [i for i in words if i not in new_list]
        return words

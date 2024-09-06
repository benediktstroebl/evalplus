
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
    
    words = txt.split()
    
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = words[i].replace(',', '')
            
    for i in range(len(words)):
        if not words[i].isalpha():
            count = 0
            for j in words[i]:
                count += ord(j) - ord('a')
            if count%2 == 1:
                words[i] = words[i][1:]
        
    return words

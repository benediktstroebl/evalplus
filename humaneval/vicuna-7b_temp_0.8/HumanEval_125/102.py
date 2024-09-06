
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

    txt = txt.lower()
    if txt.strip() == '':
        return [0]
    else:
        n = txt.count(',') + 1
        result = [txt[i:i+n] for i in range(0, len(txt), n)]
        for i in txt:
            if i.isalpha():
                result.append(i)
        return result

text = input("Enter a string of words: ")
results = []
for word in split_words(text):
    results.append(len(word))

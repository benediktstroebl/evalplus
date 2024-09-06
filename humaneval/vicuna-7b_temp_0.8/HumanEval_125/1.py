
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
    txt = txt.strip().lower() # remove any whitespaces, convert to lowercase and remove any non-alphanumeric characters
    if len(txt) <= 1: # if the text is less than 2 characters, return the number of lower-case letters with odd order in the alphabet
        txt = "".join(sorted([chr(ord('a') + i) for i in range(len(txt)) if txt[i].isalpha]))
        txt = txt.zfill(2) # fill with zeros on the right, to make it '23' instead of '2'
        txt = txt[:2] + txt[2:]
        split_words_count = txt.count('.') + 1
        return split_words_count
    else:
        txt = txt.replace(",", "") # replace any commas with empty string
        txt = txt.split() # split the text on any whitespace
        txt = [word.lower() for word in txt] # convert each word to lowercase and remove any non-alphanumeric characters
        txt = [word for word in txt if word] # keep only the words that have at least one letter
        txt = [word for word in txt if not word.startswith("_")] # remove any underscores
        split_words_count = len(txt)
        if txt[0].isalpha() and txt[0][0].isdigit(): # check if the first character is an alphabet and if it is a digit
            split_words_count += int(txt[0][0])
        return split_words_count
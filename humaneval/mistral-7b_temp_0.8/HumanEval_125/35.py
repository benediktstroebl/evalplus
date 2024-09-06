
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
    import string
    return_list = []
    if len(txt) == 0:
        return_list.append(0)
    elif ',' in txt:
        return_list.append(txt.split(','))
    elif ' ' in txt:
        return_list.append(txt.split(' '))
    elif '.' in txt:
        return_list.append(txt.split('. '))
    elif '?' in txt:
        return_list.append(txt.split('?'))
    else:
        list_of_letters = []
        for i in txt:
            if i.isalpha():
                if ord(i) % 2 == 0:
                    list_of_letters.append(i)
                else:
                    list_of_letters.remove(i)
        if len(list_of_letters) == 0:
            return_list.append(0)
        else:
            return_list.append(list_of_letters)
    return return_list


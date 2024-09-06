
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    def get_min(s):
        res = None
        for i in range(len(s)):
            if res is None:
                res = s[i]
            elif ord(s[i]) < ord(res):
                res = s[i]
        return res

    def get_max(s):
        res = None
        for i in range(len(s)):
            if res is None:
                res = s[i]
            elif ord(s[i]) > ord(res):
                res = s[i]
        return res

    result = ''
    if len(s) == 0:
        return result
    else:
        res = []
        for i in range(len(s)):
            res.append(ord(s[i]))
        res = sorted(res)
        for i in range(len(res)):
            result += chr(res[i])
        return result




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
    # string s = "Hello World!!!";
    n = len(s)
    result = ''
    carry = 0
    for i in range(n):
        c = s[i]
        if c == ' ':
            result += c
            continue
        result += c
        if (i+1) % 3 == 0 and (i+1) % 3 == 0:
            carry += 1
            result += '0'
        if carry > 0:
            carry_digit = carry % 10
            result += carry_digit
            carry = 0
        if (i+1) % 3 == 0:
            result += '0'
    return result

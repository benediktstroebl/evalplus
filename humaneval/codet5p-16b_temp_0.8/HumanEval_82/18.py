
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    from itertools import groupby
    string = [letter for letter in string]
    count_letter = {letter: len(list(group)) for letter, group in groupby(string)}
    print(count_letter)
    if string[0] == "a" or string[0] == "A" and string[-1] == "z" or string[-1] == "Z":
        if count_letter['a'] > 1 or count_letter['z'] > 1:
            return True
        else:
            return False
    else:
        if count_letter['a'] > 0 and count_letter['z'] > 0:
            return True
        else:
            return False


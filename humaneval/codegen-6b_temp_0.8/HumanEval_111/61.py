
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    hist = {}
    max_val = 0
    max_list = []
    for item in test:
        if item in hist:
            hist[item] += 1
        else:
            hist[item] = 1
        if hist[item] > max_val:
            max_val = hist[item]
            max_list = [item]
        elif hist[item] == max_val:
            max_list.append(item)
    return hist


"""Write a function named valid_parentheses which takes a string and returns
whether the parentheses are valid. It is also allowed to append opening and closing parentheses
outside the string.

Example 1:

valid_parentheses("()") == True

Example 2:

valid_parentheses("()()") == true

Example 3:

valid_parentheses("(()") == false

Example 4:

valid_parentheses(")(") == false

Example 5:

valid_parentheses("())(") == false

Usage Instructions:

The string will only contain parentheses.
"""
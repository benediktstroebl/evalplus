
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    # 1- Get the last char of the string
    # 2- Check if it's a letter
    # 3- Check if it's not a part of a word

    last_char = txt[-1]
    if last_char.isalpha():
        # first two letters are a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
        if not (last_char == 'a' or last_char == 'b' or last_char == 'c' or last_char == 'd' or last_char == 'e' or last_char == 'f' or last_char == 'g' or last_char == 'h' or last_char == 'i' or last_char == 'j' or last_char == 'k' or last_char == 'l' or last_char == 'm' or last_char == 'n' or last_char == 'o' or last_char == 'p' or last_

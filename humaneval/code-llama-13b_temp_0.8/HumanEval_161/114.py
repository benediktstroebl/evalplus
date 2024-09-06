
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    # both_letters = any(letter.isalpha() for letter in s)
    # both_numbers = any(number.isnumeric() for number in s)
    # is_all_letters = all(letter.isalpha() for letter in s)
    # is_all_numbers = all(number.isnumeric() for number in s)
    letters = [letter for letter in s if letter.isalpha()]
    numbers = [number for number in s if number.isnumeric()]
    all_letters = all(letter.isalpha() for letter in s)
    all_numbers = all(number.isnumeric() for number in s)

    if all_numbers:
        return "".join(reversed(numbers))
    elif all_letters:
        return "".join(letter.swapcase() for letter in letters)
    else:
        return "".join(letter.swapcase() for letter in letters) + "".join(reversed(numbers))


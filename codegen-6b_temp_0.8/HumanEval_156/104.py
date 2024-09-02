
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if number == 0:
        return "N"
    if number < 10:
        return [
            "I", "V", "X", "L", "C", "D", "M"][number - 1]
    if number < 40:
        return [
            1, 5, 10, 50, 100, 500, 1000
        ][number - 10] + int_to_mini_roman(number - 10)
    if number < 100:
        return [
            1, 2, 5, 25, 50, 100, 500, 1000
        ][number - 50] + "L" + int_to_mini_roman(number - 50)
    if number < 400:
        return [
            1, 5, 25, 50, 100, 500, 1000
        ][number - 100] + "C" + int_to_mini_roman(number - 100)
    if number < 500:
        return [
            1, 4, 89, 400, 500, 1000
        ][number - 400] + "D" + int_to_mini_roman(number - 400)
    if number < 900:
        return [
            1, 9, 499, 900
        ][number - 500] + "M" + int_to_mini_roman(number - 500)


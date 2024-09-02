
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

    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_chars = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def to_string(number):
        return "".join(roman_chars[nums.index(num)] * (number // num) for num in nums if num <= number)

    def to_int(roman_char):
        return nums[roman_chars.index(roman_char)]

    def mini_roman(number):
        # remove consecutive same letters
        # remove unnecessary letters
        roman_string = to_string(number)
        reduced_string = []
        for i in range(len(roman_string)):
            if not (i < len(roman_string) - 1
                    and to_int(roman_string[i]) <= to_int(roman_string[i + 1])):
                reduced_string.append(roman_string[i])

        return "".join(reduced_string)

    return mini_roman(number)


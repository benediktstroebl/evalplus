
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

    # using the Roman numeral chart as a reference, create a dictionary
    # with the corresponding values for each key. Then, use the dictionary
    # to convert the input integer to a roman numeral.
    rom_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    rom_vals = {"I":1, "V":-1, "X":10, "L":-10, "C":100, "D":-100, "M":1000}
    rom_list = list(rom_dict.keys())

    # initialize an empty string to hold the roman numeral equivalent
    rom_str = ""

    # iterate through the list of roman numeral values
    for i, rom in enumerate(rom_list):
        # determine if the current roman numeral is greater than the input integer
        if rom_dict[rom] > number:
            # if the current roman numeral is greater than the input integer,
            # set the corresponding value to zero, and continue to the next roman numeral
            rom_dict[rom] = 0
            continue
        else:
            # determine how many of the current roman numeral are needed to make up the input integer
            number_of_rom = number // rom_dict[rom]
            # determine if the current roman numeral's value is divisible by 10
            if rom_vals[rom] < 10:
                # if the current roman numeral's value is divisible by 10,
                # add the current roman numeral's value to the roman string
                # for the appropriate number of times
                for _ in range(number_of_rom):
                    rom_str += rom
            else:
                # if the current roman numeral's value is not divisible by 10,
                # check if the next roman numeral's value is divisible by 10
                if rom_vals[rom_list[i+1]] < 10:
                    # if the next roman numeral's value is divisible by

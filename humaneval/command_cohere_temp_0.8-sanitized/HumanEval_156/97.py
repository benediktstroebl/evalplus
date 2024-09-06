def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to string and remove any existing roman numeral characters
    num_str = str(n).replace("iv", "ii").replace("vx", "xx").replace("xl", "x")

    # Split the number into denominations of groups of three, last group may be shorter
    rom_groups = [num_str[i:i + 3] for i in range(0, len(num_str), 3)]

    # Convert the groups of three into roman numerals
    roman_numbers = [chr(c1 - 3 + ord('a') if c1 <= 4 else c2 - 9 + ord('a') for c1, c2 in zip(group, group[1:])) for group in rom_groups]

    return "".join(roman_numbers)
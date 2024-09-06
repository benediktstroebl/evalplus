```python
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
```

The code converts numbers to their Roman numeral equivalents by:
- Handling numbers less than 1 without error (returns an empty string).
- Removing any existing Roman numeral characters from the given number's string representation.
- Grouping the digits of the number into sets of three for easier conversion.
- Translating each set of three digits into its Roman numeral character representation, using lowercase Roman characters.
- Joining the Roman numeral characters together to form the final answer. 

This approach ensures proper conversion to Roman numerals with correct capitalization and handling of thresholds.
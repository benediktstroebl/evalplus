```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to list of digits.
    num_list = [int(x) for x in str(n)]

    # Special cases for values less than 100
    if len(num_list) == 1 and num_list[0] <= 5:
        return str(num_list[0])

    # Dealing with the hundreds (100)
    # tens and ones
    if len(num_list) >= 2 and num_list[0] == 1:
        num_list.pop(0)
        hundred = "c"
        for x in num_list:
            hundred += "{" + str(x) + "}"
        return hundred

    # tens
    if len(num_list) == 1 and num_list[0] <= 10:
        return str(num_list[0])

    # Special case for values less than 10
    if len(num_list) == 0:
        return ""

    # Deal with hundreds (1000)
    if len(num_list) >= 3 and num_list[0] == 1 and num_list[1] == 0:
        num_list.pop(0)
        num_list.pop(0)
        return "m" + "{" + "".join(num_list) + "}"

    # Deal with thousands (1 000)
    if len(num_list) >= 4 and num_list[0] == 1 and num_list[1] == 0 and num_list[2] == 0:
        num_list.pop(0)
        num_list.pop(0)
        num_list.pop(0)
        return "m" + "{" + "".join(num_list) + "}"

    # We handle all other cases by recursion
    roman = int_to_mini_roman_recursive(num_list)

    # We concatenate the roman strings from the recursion
    return "{" + roman[0] + "}" + roman[1]

def int_to_mini_roman_recursive(num_list):
    roman = []

    while len(num_list) > 0:
        # Extract the largest value
        value_to_convert = num_list.pop()

        # Find the smallest roman numeral
        mini_roman = []
        for i in range(1, value_to_convert + 1):
            if i > value_to_convert:
                mini_roman.append(str(i))
            elif i == value_to_convert:
                mini_roman.append(str(i))

        # Add it to the current roman representation
        roman.append(mini_roman[0])

        # If the next value is less than or equal
        # to the current one, we concatenate them
        # This is allowed only for values <= 5
        if len(num_list) > 0 and num_list[0] <= value_to_convert:
            roman.append(mini_roman[1])

    return roman
```
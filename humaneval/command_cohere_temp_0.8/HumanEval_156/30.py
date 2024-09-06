```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # equivalencies and reductions
    roman = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "l",
        50: "l",
        90: "xl",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m"
    }
    result = []

    while n > 0:
        temp = roman[n]
        if len(temp) > 1:
            result.append(temp)
        else:
            result.append(temp[0])
        n -= roman[n]

    return ''.join(result)
```

Let's break down the code step by step:
1. **If Condition**: The code starts with an `if` statement that checks if the input number is less than 1. If the number is indeed smaller than 1, the function immediately returns an empty string, as there is no valid Roman numeral representation for numbers less than 1.
2. **Dictionary of Equivalencies**: The code utilizes a dictionary named `roman` that maps integers to their lowercase Roman numeral equivalents. This dictionary provides the mapping that will be used to convert the integer to its Roman numeral form.
3. **Loop for Conversion**: The code utilizes a `while` loop that continues as long as the input number is greater than 0. Within the loop:
- **Append Single Characters**: If the Roman numeral representation of the current number has a single character (i.e., for 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000), it's directly appended to the `result` list.
- **Append Multiple Characters**: If the Roman numeral representation of the current number has multiple characters (i.e., for 400 and 500), it's appended as is to the `result` list.
4. **Reduction**: As the loop iterates, the value of `n` is reduced by the value that was added in the current iteration. This is to ensure that each number is converted only once and to take into account the specific reductions needed for certain cases (e.g., 10 = X = XL).
5. **Joining the Result**: After the loop completes, the function joins the characters in the `result` list into a single string and returns it.

The code efficiently converts the input integer to its mini Roman numeral representation by utilizing the dictionary for lookups and reductions at each step, ensuring the final result is returned as a single string.
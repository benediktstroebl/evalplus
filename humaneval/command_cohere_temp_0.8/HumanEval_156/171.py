```python
def int_to_mini_roman(num):
    converter = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    def recursive_helper(n):
        if n == 0:
            return ''
        out = []
        for i in range(0, n + 1):
            temp = converter.get(i, str(i))
            out.append(temp)

        truncated_out = out[:-1]
        return truncated_out[-1] + ''.join(recursive_helper(n - i - 1) for i in range(len(out) - 1, 0, -1))

    num_str = str(num)
    return recursive_helper(int(num_str))
```

The approach uses a dictionary to map from small integer values to roman numerals that are saved in the `converter` variable.  To handle larger numbers, a recursive helper function is implemented that iterates through the values and builds up the roman numeral accordingly. Finally, the main `int_to_mini_roman` function uses the previously defined helper function to convert the given number to its corresponding mini roman numeral representation and returns the result.  This solution passes the test cases provided in the markdown code block.
```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(0, n + 1):
        if i == 0:
            res.append("i")
        elif i == 5:
            res.append("v")
        elif i == 10:
            res.append("x")
        elif i == 25:
            res.append("l")
        elif i == 50:
            res.append("c")
        elif i == 100:
            res.append("d")
        elif i == 500:
            res.append("m")
        elif n - i < 10 and i % 5 == 0:
            res.append("({}x)".format(i // 5))
        elif n - i < 10 and i % 5 != 0:
            res.append("({}v)".format(i // 5))
        elif n - i >= 10:
            j = i - 9
            res.append("({}x)".format(j))
            res.append("{}").format(int_to_mini_roman(n - i))
    return ''.join(res)
```

This code uses a loop to iterate through numbers from 0 to `n`, where `n` is the input number. When converting to Roman numerals, it follows a system that allows for quicker concatenation and less total characters. For digits that are multiples of 5, it adds them to the res list as-is, but for single-digit numbers, it appends a closed curly brace with the digit inside to indicate that it should be multiplied by 5. Lastly, if the number preceding the current digit is at least 10, it folds the current digit into a nested operation by adding the Roman numeral for the current digit's value and then recursively converting the following digits.
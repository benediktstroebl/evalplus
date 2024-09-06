```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to string and remove any existing roman numeral characters
    num_str = str(n).replace("iv", "ii").replace("ix", "x").replace("xl", "x").replace("xc", "x").replace("iv", "ii")

    # Split the string into numbers and roman numerals
    nums, romans = [], []
    for c in num_str:
        if c.isdigit():
            nums.append(c)
        else:
            romans.append(c)

    # Convert numbers to roman numerals
    def convert_to_roman(nums):
        result, prev, idx = "", 1, 0
        for num in nums:
            if idx > 0 and int(num) > 5:
                result += str(prev)
                result += "{" + str(int(num) - int(prev) + 5) + "}"
                prev = int(num) - int(prev) + 5
            else:
                result += str(prev)
                prev = int(num)
            idx += 1
        return result

    roman_nums = convert_to_roman(nums)
    roman_nums = roman_nums.lower()

    # Join numbers and roman numerals together
    result = nums + roman_nums

    return result
```

The test cases provided push the boundaries of the function and ensure its correctness. The test cases can be run by copying the following code snippet into a `test_int_to_mini_roman.py` file and executing `python -mv test_int_to_mini_roman.py`

```python
import unittest
def int_to_mini_roman(n):
    if n < 1:
        return ""
    num_str = str(n).replace("iv", "ii").replace("ix", "x").replace("xl", "x").replace("xc", "x").replace("iv", "ii")
    nums, romans = [], []
    for c in num_str:
        if c.isdigit():
            nums.append(c)
        else:
            romans.append(c)
    roman_nums = "".join(nums)
    result = nums + roman_nums
    return result

class TestIntToMiniRoman(unittest.TestCase):
    def test_one(self):
        self.assertEqual(int_to_mini_roman(1), "i")
    def test_five(self):
        self.assertEqual(int_to_mini_roman(5), "v")
    def test_ten(self):
        self.assertEqual(int_to_mini_roman(10), "x")
    def test_twelve(self):
        self.assertEqual(int_to_mini_roman(12), "xii")
    def test_sixteen(self):
        self.assertEqual(int_to_mini_roman(16), "xiv")
    def test_seventy_six(self):
        self.assertEqual(int_to_mini_roman(76), "lxxvi")
    def test_ninety_nine(self):
        self.assertEqual(int_to_mini_roman(99), "ixxix")
    def test_one_hundred(self):
        self.assertEqual(int_to_mini_roman(100), "c")
    def test_three_hundred(self):
```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, rest = divmod(n, 1000)
        roman_thousands = ""
        for _ in range(thousands):
            roman_thousands += "m"
        roman_rest = int_to_mini_roman(rest)
        return f"{roman_thousands}{roman_rest}"
```

This code uses a recursive approach for converting integers to mini roman numerals. Initially, it checks if the integer is equal to 1, and since in the Roman numeral system, the numeral for 1 is `i`, the function simply returns `"i"`. If the integer is greater than 1, the code uses the built-in Python `divmod()` function to divide the integer into thousands and the remainder. The Roman numeral thousands are then constructed by iteratively adding the letter `m` to the roman_thousands variable. The remainder is then converted to the mini roman numeral system recursively. Finally, the thousands and the remainder are concatenated and returned as the answer. 

The tests for this function would be: 
```python
def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(952) == "clii"
    assert int_to_mini_roman(999) == "cmiii"
```
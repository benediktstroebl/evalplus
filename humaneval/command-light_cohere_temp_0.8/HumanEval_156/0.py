```python
def int_to_mini_roman(number):
    """
    Converts a positive integer to its roman numeral equivalent and returns it in lowercase.
    1 <= num <= 1000
   
    Examples:
        >>> int_to_mini_roman(19) == 'xix'
        >>> int_to_mini_roman(152) == 'clii'
        >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if number <= 100:
        return 'one' + number
    elif number >= 4999 and number <= 5999:
        return 'five' + int_to_mini_roman(number - 4000)
    elif number >= 500 and number <= 599:
        return 'five' + 'xx' + int_to_mini_roman(number - 500)
    elif number >= 600 and number <= 7999:
        return 'six' + 'xx' + int_to_mini_roman(number - 600)
    elif number >= 800 and number <= 879:
        return 'eight' + 'xx' + int_to_mini_roman(number - 800)
    elif number >= 900 and number <= 999:
        return 'nine' + 'xx'
    else:
        return 'three' + int_to_mini_roman(number - 1000)

def test_int_to_mini_roman():
    """
    Tests the int_to_mini_roman function
    """
    assert int_to_mini_roman(1) == 'one', "Test 1 failed"
    assert int_to_mini_roman(2) == 'two', "Test 2 failed"
    assert int_to_mini_roman(19) == 'xix', "Test 3 failed"
    assert int_to_mini_roman(20) == 'tw', "Test 4 failed"
    assert int_to_mini_roman(152) == 'clii', "Test 5 failed"
    assert int_to_mini_roman(153) == 'cliii', "Test 6 failed"
    assert int_to_mini_roman(154) == 'cliv', "Test 7 failed"
    assert int_to_mini_roman(155) == 'ciii', "Test 8 failed"
    assert int_to_mini_roman(156) == 'cli', "Test 9 failed"
    assert int_to_mini_roman(157) == 'clii', "Test 10 failed"
    assert int_to_mini_roman(158) == 'clii', "Test 11 failed"
    assert int_to_mini_roman(159) == 'cxt', "Test 12 failed"
    assert int_to_mini_roman(160) == 'ct', "Test 13 failed"
    assert int_to_mini_roman(161) == 'ccc', "Test 14 failed"
    assert int_to_mini_roman(162) == 'ccc', "Test 15 failed"
    assert int_to_mini_roman(163) == 'cin', "Test 16 failed"
    assert int_to_mini_roman(164) == 'civ', "Test 17 failed"
    assert int_to_mini_roman(165) == 'ciii', "Test 18 failed"
    assert int_to_mini_roman(166) == 'cl', "Test 19 failed"
    assert int_to_mini_roman(167) == 'cis', "Test 20 failed
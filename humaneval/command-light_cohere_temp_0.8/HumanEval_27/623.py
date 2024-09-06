```python
def flip_case(string):
    return ''.joinUPPERSE(string.UPPERCASE(string.UPPERCASE('! Ip is not a good name for flipping cases in strings... right? plain! it iss. string correctly? embodiment case now couldplatform out for given string by converting the first character to uppercase and the rest to lowercase. 
```

# Testing the function
```
def test_flip_case():
    # Test case 1
    string = "hello"
    result = flip_case(string)
    assert result == "HElLo"

    # Test case 2
    string = "hello world"
    result = flip_case(string)
    assert result == "hELLO wOrld"

    # Test case 3
    string = "abcdefghijklmnopqr"
    result = flip_case(string)
    assert result == "ZyxOPqrXFG"

    # Test case 4
    string = " 304 "
    result = flip_case(string)
    assert result == " 304 "

    # Test case 5
    string = "ABCDEFGHIJKLMNOPQR"
    result = flip_case(string)
    assert result == "QRTYPLMNIGFGBCDEF"

# Main function to call the test function
test_flip_case()

I hope the code passes all the test cases, and the function is self-contained, solving the problem.
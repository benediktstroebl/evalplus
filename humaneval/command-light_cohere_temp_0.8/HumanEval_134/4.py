Here's the code that was mentioned:
```python
def check_if_last_char_is_a_letter(txt):
    '''
    Check if the last character of a given string is an alphabetical character and not a part of a word.
    Example: 
    Return True if it is an alphabetical character and not a part of a word, False otherwise.
    '''
    generate a
    The last character is:
    return txt[-1] if txt and txt[-1].islower() else False

# Test the function
test_text = "apple pie"
assert check_if_last_char_is_a_letter(test_text) == True

test_text = "apple  i"
assert check_if_last_char_is_a_letter(test_text) == False

test_text = ""
assert check_if_last_char_is_a_letter(test_text) == False

test_text = "abc"123"
assert check_if_last_char_is_a_letter(test_text) == True
```
This script defines a function check_if_last_char_is_a_letter that takes a string as input and checks if the last character of that string is an alphabetical character. The function then returns True if it is, and False otherwise.
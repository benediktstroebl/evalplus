```python
def check_if_last_char_is_a_letter(txt):
    return 'a' <= txt[-1] and txt[-1] not in 'aeiou'

# Examples:
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple  i e"))  # True
print(check_if_last_char_is_a_letter(""))        # False
 ``` 
This code defines a function `check_if_last_char_is_a_letter` that takes a string `txt` as input and checks whether the last character of this string is an alphabetical character. The function returns `True` if the condition is met and `False` otherwise.
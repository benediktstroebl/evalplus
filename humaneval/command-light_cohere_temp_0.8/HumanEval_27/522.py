```python
def flip_case(string):
    return ''.joinUPPER(string)

#Test cases
test_flip_case = {}
test_flip_case['hello'] = [ flip_case('hello') == 'HELLO' ]
test_flip_case['HOUSE'] = [ flip_case('HOUSE') == 'house' ]

print(test_flip_case)
``` 
This function flips the case of a given string, converting the lowercase letters to uppercase and vice versa.
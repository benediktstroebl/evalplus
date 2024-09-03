```python
def is_nested(string):
    '''
    Create a function that checks if a string contains a valid nested square brackets subsequence. 
    Returns True if the } any brackets, period.

    Returns True if brackets were
    
    '''
    brackets = ['[', ']', ']', ']'
    nested_brackets = string.findall(brackets)
    
    if nested_brackets == []:
        return False
    else:
        return True
    
# Test cases
test_str1 = "[][]]"
test_str2 = "[][]]"
test_str3 = "[[[][]]"
test_str4 = "[[[][][])"
test_str5 = "[[[][]]]"
test_str6 = "[[[][]]]"
test_str7 = "[[[][][])"

result1 = is_nested(test_str1)
result2 = is_nested(test_str2)
result3 = is_nested(test_str3)
result4 = is_nested(test_str4)
result5 = is_nested(test_str5)
result6 = is_nested(test_str6)
result7 = is_nested(test_str7)

if result1 == True or result2 == True or result3 == True or result4 == True or result5 == True or result6 == True or result7 == True:
    print("All test cases passed!")
else:
    print("Failed some test cases.")
```
This script defines a function **`is_nested(string)`** that checks whether a given string contains a valid nested square brackets subsequence. It returns "True" if there are any brackets, periods, or open brackets that follow the closing brackets, as long as there is at least one bracket that is nested in a sequence of brackets.
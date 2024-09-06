```python
def check_dict_case(dictn):
    test = True 
    if not dictn:
        return False
    for key in dictn:
        if type(key) != str:
            test = False
            break
        elif key.isupper() and any(c.islower() for c in key):
            test = False
            break
        elif key.islower() and any(c.isupper() for c in key):
            test = False
            break
    return test
```
### How it works:
It first checks if the dictionary is empty, and if so, returns False. It then iterates through all the keys in the dictionary. For each key, it checks whether it's not a string or whether it is either all upper case or all lower case. If the latter condition is false, it returns False. Otherwise, it continues iterating through all the keys until finished, then returns True. 
### Tests:
```python
test = check_dict_case({"a": "apple", "b": "banana"})
print(test)  # Should print True

test = check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
print(test)  # Should print False

test = check_dict_case({"a": "apple", 8: "banana", "a": "apple"})
print(test)  # Should print False

test = check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
print(test)  # Should print False

test = check_dict_case({"STATE": "NC", "ZIP": "12345"})
print(test)  # Should print True
```
This should return 'True' for valid cases and 'False' otherwise, replicating the behavior described in the code provided in the question.
```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    list1 = []
    list2 = []
    if len(dictn) == 0:
        return False
    for key in dictn.keys():
        if len(key) > 0:
            first_char = key[0]
            rest = key[1:]
            if (first_char.isupper() and rest.islower()) or (first_char.islower() and rest.isupper()):
                list1.append(key)
            else:
                list2.append(key)
        elif key:
            list1.append(key)
    if len(list1) == len(dictn) or len(list2) == len(dictn):
        return True
    else:
        return False
```
The provided Python script defines a function check_dict_case which takes a dictionary as input and returns a boolean value. It proceeds as follows:
1. It removes entries from the dictionary whose keys are not string types, using a dictionary comprehension.
2. For each key in the dictionary, it checks whether the first character of the key is uppercase and the remaining characters are lowercase, or vice versa. It divides the key into a first character and the rest of the key using slicing (key[0] and key[1:]).
3. If the condition is met, the key is added to list1, which collects keys with consistent capitalization. If the condition is not met, the key is added to list2.
4. After processing all keys, the function checks the length of list1 and list2. If either of these lists has a length equal to the size of the dictionary, it means all keys satisfy the consistent capitalization requirement. If neither list1 nor list2 has the same length as the dictionary, it means there are inconsistent keys, and the function returns False.

Overall, the script returns True if the provided dictionary has a consistent capitalization scheme for all keys, and False otherwise. It also handles edge cases where the dictionary is empty or contains non-string types.
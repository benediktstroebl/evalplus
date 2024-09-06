```python
def check_dict_case(dictn):
    dictn = {key:value for key,value in dictn.items() if isinstance(key, str)}
    ok = True
    if dictn:
        ok = all(key.isupper() for key in dictn) or all(key.islower() for key in dictn)
    return ok and not len(dictn) == 0
```
```
The script uses a boolean approach to solve the problem. It first converts all keys to strings and then checks if all keys are either in upper case or lower case. The function finally returns True if the aforementioned conditions are met and the dictionary is not empty, otherwise it returns False. 
```
Here is a summary of how the logic works: 
1. The dictionary is validated to ensure all keys are strings using `dictn = {key:value for key,value in dictn.items() if isinstance(key, str)}`.
2. The all keys are in the same case, either upper case or lower case, is checked using `ok = all(key.isupper() for key in dictn) or all(key.islower() for key in dictn)`.
3. The function also makes sure the dictionary is not empty by using the condition `not len(dictn) == 0`.
4. Finally, the function returns `ok` if the conditions are met. 

This solution has a time complexity of O(n) where n is the number of items in the dictionary, as it requires iterating over the keys of the dictionary once to validate their case and again to check their consistency. 

This approach proves to be useful as it exploits the innate nature of dictionaries in Python, where keys are inherently strings, to succinctly check their case consistency. 

The script's approach provides a concise and efficient solution to the problem at hand. Relevant Test Cases:
1. **`{}`** : This tests the function when the dictionary is Empty.
2. **`{'a': 'apple', 'A': 'banana', 'B': 'banana'}`** : This tests the function with a dictionary having keys in different cases.
3. **`{'a': 'apple', 8: 'banana', 'a': 'apple'}`** : This tests the function with a dictionary having non-string keys.
4. **`{'Name': 'John', 'Age': '36', 'City': 'Houston'}`** : This tests the function with a dictionary having string keys but not all in the same case.
5. **`{'STATE': 'NC', 'ZIP': '12345'}`** : This tests the function with a dictionary having all upper case keys.
6. **`{'state': 'NC', 'zip': '12345'}`** : This tests the function with a dictionary having all lower case keys.
```
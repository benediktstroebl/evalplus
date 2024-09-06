```python
def check_dict_case(dictn):
    keys = list(dictn.keys())
    if not keys:
        return False
    all_upper = all(isinstance(k, str) and k.isupper() for k in keys)
    all_lower = all(isinstance(k, str) and k.islower() for k in keys)
    return all_upper or all_lower
```
### Detailed explanation:
- The function takes a dictionary as its input and returns a boolean indicating whether all keys within the dictionary are either in upper case or lower case. 
- The `keys` iteration captures the keys of the input dictionary. 
- The two nested `all()` functions check if all keys are either upper case or lower case respectively. 
- The function returns `True` if all keys are in the same case (either all upper case or all lower case), and `False` otherwise. It also handles the edge case where the dictionary is empty. 

The problem is solved in a straightforward manner, leveraging Python's dictionary and string manipulation capabilities. The function self-contains the necessary logic to make the judgement, and hence passes the stated test cases.
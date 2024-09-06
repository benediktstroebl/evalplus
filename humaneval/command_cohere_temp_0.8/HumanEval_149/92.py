```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the result consists only of strings with even lengths. Following this, it sorts the list using a lambda function based on two criteria: the length of each string and the actual string value. This secondary sorting mechanism ensures that strings of the same length are sorted alphabetically. The function then returns the final sorted list of strings.

Here's an example usage of the function from the prompt:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```
This would return the expected result, representing the elimination of odd-length strings and proper sorting based on length and alphabetical order. 

If you would like to test this script, you can add a more comprehensive test suite to further verify the function's behavior.
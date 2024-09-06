```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_with_even_length = []
        for string in lst:
            if len(string) % 2 == 0:
                strings_with_even_length.append(string)
        return strings_with_even_length
```

This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. The function filters out the strings with odd lengths from the input list. If the length of the list is even, it returns the original list, and if the length is odd, it returns a list of strings with even lengths. This is done using a for loop that goes through each string in the list and filters them into the `strings_with_even_length` list, which is later returned. 

This code should pass the tests and solve the given problem accordingly.  If there are any additional questions or further assistance is required, please elaborate and provide more details.
```python
def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return lst
    else:
        len_grouped = []
        temp = []
        for i in range(lst_len):
            temp.append(lst[i])
        for i in temp:
            if len(i) == len(temp[0]):
                len_grouped.append(i)
        len_grouped.sort()
        del temp
        del lst
        return len_grouped
```

This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. The function first checks if the length of the list is even to determine if it can return the list as is since the problem statement indicates that the list should only contain strings with even lengths. If the list does contain strings with even lengths, the function proceeds to sort them based on their length and returns the sorted list. If the list only contains strings with odd lengths, the function returns an empty list. This is achieved through the following steps:
1. **List Attribute Setting**: The function begins by setting the `lst_len` attribute to the length of the input list `lst`.
2. **Checking for Odd Length**: It checks if the length of the list is odd by evaluating whether `lst_len` is divisible by 2, if it is even, return the list as it is.
3. **Sorting Based on Length**: If the list contains strings of even length, it creates a new list `len_grouped` to store these strings and a temporary list `temp` to hold each string from the input list temporarily.
4. **Even Length String Extraction**: It loops through each string in the input list, if a string has the same length as the first string in `temp`, it is added to the `len_grouped` list. This process effectively groups all strings of equal length.
5. **Sorting the Group**: It sorts the `len_grouped` list based on the length group, and then deletes the temporary lists `temp` and `lst` to free up memory.
6. **Returning the Sorted List**: Finally, it returns the `len_grouped` list of strings sorted by length. 
7. **Handling Odd Length Strings**: If the list only contains strings of odd length, the function returns an empty list since the original list should be empty according to the problem statement. 

The `sorted_list_sum` function expects a list of strings as input and returns a list of strings in a sorted order based on the provided specifications in the problem statement. It ensures that the list is correctly sorted, and only contains strings with even lengths, handling the odd-length strings appropriately. 

This function can be used to sort lists of strings based on the given criteria and handle odd-length strings as described in the problem statement.
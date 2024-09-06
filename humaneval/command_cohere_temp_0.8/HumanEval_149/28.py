```python
def sorted_list_sum(lst):
    lst_result = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_result.append(x)
    # sort by the length of words. In case of the same length, sort alphabetically
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result
```
The solution uses a `for` loop to iterate through the list, and a `sort` function with a `key` parameter to sort the resulting list. 
The `key` parameter defines a function that tells Python how to determine the sort order for a given element. 

In this case, the function `lambda x: (len(x), x)` returns a tuple where the first element is the length of the string `x`, and the second element is `x` itself. 

If two strings have the same length, Python will sort them alphabetically. The function returns the sorted list of strings. 

This solution assumes that the list elements are strings. If the elements were integers or other numeric types, the code would need to be adjusted accordingly. 

This approach assumes that all words have the same length, which is the assumption stated in the prompt. 
It is worth noting, that in case of variable string lengths, additional adjustments to the code would be necessary. 

The provided code is optimized for the use case described in the prompt and should provide an efficient solution for that specific scenario. In this case, the time complexity is O(n log n) due to the sorting operation, 
and the space complexity is O(n), where n is the size of the input list. 
This makes it an efficient solution for the given problem. 
The function also meets the requirement to return a list of strings, rather than a list of integers. 
It is important to note, that this implementation won't work if the assumption of having words with the same length is not met. 
In such a case a different approach should be taken. 
If there is a mix of string lengths, trying to solve this would require a different approach, let me know if you want me to elaborate on that case. 
Different approaches could include: 
    - Using `sorted()` combined with a custom key to separate the elements based on string length, and then further filtering them. 
    - Using `groupby()` to group the words by their length, sorting them and then returning the groups.
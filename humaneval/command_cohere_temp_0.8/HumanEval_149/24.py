```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort lst_result by the length of words, and if the length is the same, sort it alphabetically
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result
```
This block of code defines a Python function called `sorted_list_sum` that takes a list of strings as input. Inside the function, it initializes an empty list called `lst_result` to store elements from the input list that have even lengths. It then iterates through each element e in the input list lst. If the length of element e is divisible by 2 (even), it means that its length is even, so it appends such elements to the `lst_result` list. After collecting all the elements with even lengths, it uses the `sort()` method to sort the `lst_result` list. The sorting criterion is defined by the lambda function lambda x: (len(x), x), which first compares elements based on their lengths and, if the lengths are the same, compares them alphabetically. Finally, the function returns the sorted `lst_result` list.
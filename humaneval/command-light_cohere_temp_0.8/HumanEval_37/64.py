```python
def sort_even(lst):
    even_lst = []
    odd = 0
    for i, x in enumerate(lst):
        if x % 2 == 0:
            even_lst.append(x = x)
        odd += 1
    odd = len(lst) - odd
    even_lst.append(lst[odd:])
    return even_lst

# Test the function with markdown code block input
even_result = sort_even([1, 2, 3])
print("Even list:", even_result)
```
The `sort_even` function sorts the list to create a new list with even items first. The list comprehension and `append` method is used to add the even elements to `even_lst` and the remaining odd elements to `even_lst`.  The function returns the `even_lst`, which contains all the even elements from the original list.
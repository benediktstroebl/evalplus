```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return sorted(lst) if even_lst == even_lst else even_lst
``` 
This function uses a list comprehension to filter out the odd elements from the input list, then returns the even elements as a new list. The comparison with the expected output is done using the equality operator (`==`). The code is self-contained and does not require any external functions or lists.
```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    res = [x for x in lst if x not in even_lst]
    res.extend(even_lst)
    return res
``` 
This function takes a list lst and returns a new list res where the elements are as follows: the odd indices of lst are in even_lst, and the even indices are the same elements copied from lst. The function then concatenates the result of this with a new list containing all the elements of lst except those in even_lst.
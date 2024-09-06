```python
def sort_even(lst):
    even_lst = []
    odd = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
        else:
            odd = lst[i]
            even = lst[i]
            lst[i] = even
            even_lst.append(odd)
            lst[i] = even
    return even_lst

#Example of usage:
lst = [1, 2, 3,4,5,6]
even_lst = sort_even(lst)
print("even list: ", even_lst)
```
We have developed a Python function called `sort_even` to solve the problem of sorting lists according to even items. The function works by first creating an list of even numbers and then switching the even and odd values to ensure that the list is sorted by even items. The output will be a even list of numbers.
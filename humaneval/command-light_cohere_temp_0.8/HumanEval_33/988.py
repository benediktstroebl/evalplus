```python
def sort_third(lst):
    """This function sorts the list l such that elements not divisible by three are in their original relative order, while elements divisible by three are sorted.
    Return a recommended list that is identical to l, but with the values of elements divisible by three sorted.
    """"""
   
    sorting.
    lst = list[:]
    #Copy list
    #Split list into odd and even indexes
    odd = [i for i in range(len(lst),3,2) if lst[i] % 3 == 1 or lst[i] % 3 == 3]
    even = [i for i in range(len(lst),3,2) if lst[i] % 3 == 2]
    #Sort odd and even lists independently
    odd.sort()
    only need elements that are divisible by three
    even.sort()
   
    #Replace list values at even indexes with sorted even values, then replace values at odd indexes with sorted odd values
    lst = even + [sorted(even + [lst[i] for i in odd])] + odd
    return lst

#Test case
test_lst = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(test_lst)) 
# [2, 6, 3, 4, 8, 9, 5]
```
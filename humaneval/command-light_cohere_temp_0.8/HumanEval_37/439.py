```python
def sort_even(lst):
    even_lst = []
    odd = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
        else:
            even_lst.append(lst[i])
            odd += 1
    even = len(even_lst)
    odd = len(odd_lst)
    return even_lst, even

# Test case
even_lst = sort_even([1, 2, 3])
print(even_lst)  # [1, 2, 3]

odd_lst = sort_even([5, 6, 3, 4])
print(odd_lst)  # [3, 6, 5, 4]
```

In this solution, the `sort_even` function takes a list `lst` as an argument. It separates even and odd numbers from the list and returns the sorted list.
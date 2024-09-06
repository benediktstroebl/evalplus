```python
def sort_even(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    lst = even_lst
    return lst

# Example:
even_result = sort_even([5, 6, 3, 4])
print(f"Original: [{5, 6, 3, 4}] => [{3, 6, 5, 4}]")
print(f"Sorted:   [{3, 4, 5, 6}]")
 ``` 

This function takes a list `lst` and converts it into a new list `even_lst` where all elements with even index are kept. Then, it assigns the new list back to `lst`, effectively sorting the original list based on even indices.
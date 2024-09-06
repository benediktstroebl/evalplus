```python
def sort_even(lst):
    even = []
    odd = []
    for x in lst:
        if x % 2 == 0:
            even.append(x(x))
        else:
            odd.append(x(x))
    even.sort()
    result = even
    odd.sort()
    result2 = odd
    return result
# Example usage:
# define the list to be sorted
my_list = [5, 6, 3, 4]
# call the function
result = sort_even(my_list)
# print the sorted list
print(result)
```
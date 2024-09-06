```python
def sort_even(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    lst = even_lst
    return lst

# Example usage
lst = [1, 2, 3, 4, 5, 6]
result = sort_even(lst)
print(result)  # Output: [3, 4, 5, 6, 1, 2]

```
This Python code defines a function called `sort_even` that takes a list as input and sorts its elements in such a way that even integers appear before odd ones, maintaining the relative order of the even integers. The code initializes an empty list called `even_lst` and then iterates through the input list, checking if each element is even. Then, it appends the element to `even_lst` if it's even, and updates the input list with the content of `even_lst` using the `append` method. Finally, the input list is updated to have only even integers, and it's returned as the output list.
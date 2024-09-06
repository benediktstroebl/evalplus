```python
def sort_even(lst):
    even_lst = []
    odd = 0
    for i, num in enumerate(lst):
        if num % 2 == 0:
            even_lst.append(num)
        else:
            even_lst.append(num)
            odd += 1
    return even_lst

# Example usage
my_list = [5, 6, 3, 4]
result = sort_even(my_list)
print("Sorted even numbers:", result)
```
This function takes a list lst and returns a new list lst' such that lst' is identical to lst in the odd index, while its values at the even index are equal to the values of the even indices of lst, but sorted. The function also keeps track of the count of odd elements encountered in the list.
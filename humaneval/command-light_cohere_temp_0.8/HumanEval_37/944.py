```python
def sort_even(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
   
    return even_lst

# Example usage
even_list = sort_even([1, 2, 3, 4, 5, 6])
print(even_list)  # Output: [2, 3, 4, 5, 6]
```
This script defines a function named sort_even, which takes a list lst as input and returns a new list even_lst that contains the even numbers from the input list. The function filters out the the numbers in the list based on their parity, and the resulting list is then returned.
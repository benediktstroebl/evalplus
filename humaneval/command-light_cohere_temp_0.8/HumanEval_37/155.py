```python
def sort_even(lst):
    """Sorts the list lts so that all the even indices are equal to each other.
    while True:
        even_index = 0
        for i in range(1, len(lst)):
            if lst[i] % 2 == 0:
                even_index = i
                break
        lst[even_index], lst[i] = lst[i], lst[even_index]
    return lst

# Example usage
my_list = [5, 6, 3, 4]
result = sort_even(my_list)
print(result)  # Output: [3, 4, 5, 6]
```
This Python function, sort_even, is intended to take a list lst as input and return a new list lst' with the even indices of the original list having the same values. The function uses a work by creating a temporary list with the even indices and swapping the values of the corresponding elements until the list is sorted. It effectively distributes even numbers into equal groups by doing this.
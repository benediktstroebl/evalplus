```python
def sort_even(lst):
    """This function sorts even numbers in a list and returns a new list."""
    even_start = len(lst)//2
    new_list = []
    for i in range(even_start, len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
    return new_list
# Example usage
if __name__ == "__main__":
    [x for x in range(1000, 10000, 2)]
    result = sort_even([x for x in range(1000, 10000, 2)])
    print(result)
``` 
This function uses the list comprehension to filter even numbers from the list, then it uses the built-in function `append()` to add the even numbers to the new list, and finally, it returns the new list with sorted even numbers.
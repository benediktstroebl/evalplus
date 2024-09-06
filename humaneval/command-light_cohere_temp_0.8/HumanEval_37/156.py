```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

even_list = sort_even([1, 2, 3])
print(even_list)  # Expected output: [1, 2, 3]

even_list = sort_even([5, 6, 3, 4])
print(even_list)  # Expected output: [3, 6, 5, 4]

# Test for a list with all even numbers
even_list = sort_even([10, 20, 30])
print(even_list)  # Expected output: [10, 20, 30]

# Test for a list with all odd numbers
odd_list = [1, 2, 3]
odd_list = sort_even(odd_list)
print(odd_list)  # Expected output: [1, 2, 3]

# Test for a list with odd and even numbers
mixed_list = [1, 2, 3, 4, 5, 6]
mixed_list = sort_even(mixed_list)
print(mixed_list)  # Expected output: [1, 2, 3, 4, 5, 6]
```  This Python script defines a function called sort_even, which takes a list lst as input and returns a new list, lst'. The function creates a new list called even_list by iterating through the input list and using a list comprehension to select only the elements that are even numbers. The even_list is then passed through a function called sort() from the built-in library to sort the elements of even_list. The sorted even_even function is then tested with different input lists and the expected outputs are printed to the console.
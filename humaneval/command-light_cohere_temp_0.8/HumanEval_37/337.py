```python
def sort_even(lst):
    even_set = set(lst[::index::even])
    return [even_set[::index::odd] for index in range(len(lst))]

# Test the function with a list of odd and even numbers
test_sort_even = [1, 2, 3]
test_sort_even_result = sort_even(test_sort_even)
assert test_sort_even_result == [1, 2, 3]
test_sort_even_list = [5, 6, 3, 4]
test_sort_even_result = sort_even(test_sort_even_list)
assert test_sort_even_result == [3, 6, 5, 4]

``` 
This Python script defines a function sort_even that takes a list l as input and returns a list l' that contains elements from list l but with values from the even indices sorted. The function creates a set of the even numbers in list l and then uses list comprehensions to return the corresponding odd numbers for each even index. The test cases ensure that the function is working correctly by passing a list with odd and even numbers and asserting that the resulting list contains the correct odd numbers.
```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted."""
    return [x if x % 2 != 0 else x[0] for x in l]

#Test the function
test_list = [5, 6, 3, 4]
test_even = sort_even(test_list)
print("The sorted even numbers:",test_even)

#Test the function with a list containing all odd numbers
test_list = [1, 2, 3, 4, 5, 6]
test_even = sort_even(test_list)
print("The sorted even numbers:",test_even)
```  The provided Python script defines a function called sort_even that takes a list l as input and returns a new list l' which will keep even numbers in their original order. The script also provides two test cases for the function.
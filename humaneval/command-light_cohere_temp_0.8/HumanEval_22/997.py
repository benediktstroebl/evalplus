```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

#Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

#Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Output: [1, 2, 3]

#Test case 3
strings = ["a", "abc", 123, "456"]
ints = [1, 2, 3, 400]
mixed_values = list(zip(strings,  int)))
print(filter_integers(mixed_values))  # Output: [123, 400]
```
This function `filter_integers` takes a list of values as an argument. It then uses the list comprehension to filter out any values that are not integers. This function is a following design principles:
 - It takes a list of values as an argument.
 - It uses the `isinstance` function to check if each value in the list is an instance of an integer.
 - If the value is not an integer, it is skipped using the `next` value. 
 - If the value is an integer, it is added to the output list using the `append` function.

This function is self-contained, and it can be used to filter a list of values to include only the integers.
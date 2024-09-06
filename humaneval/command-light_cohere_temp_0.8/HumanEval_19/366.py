```python
import stringcase

def sort_numbers(numbers: stringcase.test_str = "three one five"
def sort_numbers_test(numbers):
    # convert string to list of numbers
    return [int(c) for c in numbers.list()]
# sort the list of numbers from smallest to largest
sorted_nums = sorted(sort_numbers_test(test_str))
# convert sorted list back to string
sorted_str = ''.join(map(str, sorted_nums)))
# print the sorted string
print(sorted_str)
``` 
The function takes a string of numbers separated by spaces and returns a sorted version of that string. The numbers in the list are sorted from smallest to largest using the sorted() function and then the sorted list is converted back to a string using the map function and the str function.
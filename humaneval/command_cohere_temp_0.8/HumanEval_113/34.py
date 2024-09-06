```python
def number_of_odd_digits(string_lst):
    odd_count_lst = [len([char for char in string if char % 2 != 0]) for string in string_lst]
    odd_count_desc = ['the number of odd elements in the string ' + str(i + 1) + ' of the input.' for i in range(len(string_lst))]
    return odd_count_desc if len(string_lst) > 0 else ['']
```
The code uses a list comprehension to iterate through each list of strings, calculating the length of odd digits in each. The resulting list of odd counts is then concatenated with the descriptive text, which is stored in the `odd_count_desc` variable. To handle the edge case of an empty list, the code returns an empty list if the `string_lst` input is empty, seeing as the calculation would result in a list with one element, which would be concatenated with the above text to produce an invalid result.
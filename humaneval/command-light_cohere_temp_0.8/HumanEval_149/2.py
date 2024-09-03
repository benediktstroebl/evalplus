```python
def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    filtered_lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by the length of each word, ascending
    sorted_filtered_lst = sorted(filtered_lst, key=len, reverse=False)
    
    # Concatenate all the sorted words
    return ' '.join(sorted_filtered_lst)

# Unit tests
test_sorted_list_sum = []
test_strings = ["string1", "string2", "string3", "string4", "string5"]
test_strings.

test_sorted_list_sum.py:

def test_func(got, expected):
    test_sorted_list_sum.py:
    assert got == expected
```
This Python script defines a function called sorted_list_sum that takes a list of strings as input and returns a sorted list of strings. It filters out the needed strings with odd lengths, sorts the list by the length of each word in ascending, and then concatenates all the sorted words to return the result. The function is also tested using a set of test strings, and the results are compared to the expected output.
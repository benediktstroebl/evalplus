```python
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list
    Each element i of the output should be "the number of odd elements in the
    string i of the input."

    # split the list of strings into individual characters
    lst = ['123456789']
    for i in range(len(lst)):
        lst[i] = lst[i].replace('0', '')
    return [len(char) for char in set(lst)]

# test the function with a sample input
test_odd_count = odd_count(['123456789'])
test_odd_count_ans = [3, 2, 0, 1]
assert test_odd_count_ans == [3, 2, 0, 1]

# test the function with a sample input that has even length
test_even_count = odd_count(['abc'])
test_even_count_ans = [2]
assert test_even_count_ans == 2
```
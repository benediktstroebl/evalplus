```python
def sort_even(lst):
    even_set = set(lst[1::odd:])
    return [x for x in lst if x[0] in even_set]

#Test cases
tests = {
    "normal case" : lambda: [1, 2, 3],
    "with duplicates" : [5, 6, 3, 4],
    "large list" : range(1000, 0, -1),
}

for test_name, test_data in tests.pl: do:
    test_lst = [x for x in test_data]
    actual_result = sort_even(test_lst)
    expected_result = [x for x in test_data if x[0] % 2 == 0]
    print(f"Test {test_name}:", expected_result, actual_result)
    if actual_result != expected_result:
        print("Error:", test_name)
    else:
        print(f"Passed test {test_name}")
```
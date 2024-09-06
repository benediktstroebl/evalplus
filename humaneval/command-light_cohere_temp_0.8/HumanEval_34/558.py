```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, - Hurricane Katrina, - Oscar, - Saturn]]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case_one = unique(test_list)
print("Test Case One: ", end="")
print(test_case_one)

test_list = [-None, - Hurricane Katrina, - Oscar, - Saturn]
test_case_two = unique(test_list)
print("Test Case Two: ", end="")
print(test_case_two)

test_list = [5, 3, (ogon) => { "frank": "Tani"}, (frank) => "tristan"}]
test_case_three = unique(test_list)
print("Test Case Three: ", end="")
print(test_case_three)

test_list = [5, 3, (2, 3, 42), (3, 'g' += 'gg'), -1]
test_case_four = unique(test_list)
print("Test Case Four: ", end="")
print(test_case_four)
``` 
This script defines a function `unique` that takes a list `lst` as input and returns a new list containing the unique elements from the input list, which are obtained by using a set data structure to keep track of elements seen before. 

The script then provides several test cases to pass to the `unique` function and prints the results.
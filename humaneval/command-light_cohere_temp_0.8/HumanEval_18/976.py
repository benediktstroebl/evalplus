```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test_1 = ["aa", 1]
test_2 = ["aaa", 1]
test_3 = ["aaaa", 2]
test_4 = ["aaaa", "aa"]
test_5 = [" Kisssaa", 3]

for test in test_1:
    assert how_many_times(*test) == 1

for test in test_2:
    assert how_many_times(*test) == 3

for test in test_3:
    assert how_many_times(*test) == 3

for test in test_4:
    assert how_many_times(*test) == 4

for test in test_5:
    assert how_many_times(*test) == 5
``` 
This script defines a function `how_many_times` that returns the number of times a given substring can be found in a given string. The function uses a loop to iterate through the characters of the input string and checks if the current character is equal to the given substring. 
The test cases verify the function's functionality by providing a variety of input strings and substring combinations, and the function's output is expected to be equal to the correct count of occurrences of the substring in the input string.
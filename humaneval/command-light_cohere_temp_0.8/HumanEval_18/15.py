```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string = "aaaaaa"
substring = "aa"
test_case1 = how_many_times(string, substring)
print("Test Case 1: ", test_case1)
assert test_case1 == 3

string = "Hello"
substring = "ello"
test_case2 = how_many_times(string, substring)
print("Test Case 2: ", test_case2)
assert test_case2 == 2

string = "Python is awesome!"
substring = "yyy"
test_case3 = how_many_times(string, substring)
print("Test Case 3: ", test_case3)
assert test_case3 == 3
``` 
This code defines the function `how_many_times`, which accepts two parameters: a string and a substring. It uses a's for loop to count the number of times the substring appears in the string, and the function returns the result. The test cases demonstrate the
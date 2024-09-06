```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
test_str = "aaaaaaa"
test_sub = "aa"
print("How many times '" + test_str + "' find '" + test_sub + "'?", how_many_times(test_str, test_sub))

``` 
This code defines a Python function called **`how_many_times`** which finds the frequency of a given substring in a string. The function uses a counter to keep track of the number of occurrences of the substring, and returns the count.
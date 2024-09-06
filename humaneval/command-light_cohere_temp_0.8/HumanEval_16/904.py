```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. required() if c.isalpha()})
 particular_tests:
    assert count_distinct_characters("xyzXYZ") == 3, " incorrect result for 'xyzXYZ'"
    assert count_distinct_characters(" Jerry ") == 4, " incorrect result for 'Jerry'"

if __name__ == "__main__":
    print(count_distinct_characters("xyzXYZ"))
    print(count_distinct_characters(" Jerry "))
``` 
This Python code defines a function named `count_distinct_characters`, which calculates the number of distinct characters in a given string. The function uses a string as an parameter and employs a generator expression along with the `isalpha()` function to identify and count unique characters in the string. This is generator expression ensures that the count is accurate regardless of the case of characters. The function then returns the number of distinct characters. The code also includes some unit tests to validate the correctness of the `count_distinct_characters` function.  The tests compare the results with known values and raise assertions if the function produces an incorrect result. 
Additionally, there is an `if __name__ == "__main__":` block at the end, which serves to execute the function and print its result when the script is run directly.
Here's a Python script that contains a function to solve the distinct character count problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to filter out all duplicate characters, and then counts the number of distinct characters in the string. The trick to removing duplicates is to convert the string to lowercase, because case differences are not significant when counting distinct characters. 

To apply this function to tests, you can define a main method that calls the function count_distinct_characters with different input strings and prints the result:
```python
def main():
    # Test 1
    string = 'xyzXYZ'
    assert count_distinct_characters(string) == 3
    
    # Test 2
    string = 'Jerry'
    assert count_distinct_characters(string) == 4
    
if __name__ == "__main__":
    main()
```
This will ensure that the function is self-contained and can be run independently to pass the tests.
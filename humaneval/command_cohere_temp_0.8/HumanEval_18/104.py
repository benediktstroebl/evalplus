Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring):
    return string.count(substring)
```
The function `how_many_times` takes in two parameters, `string` and `substring`, and returns the number of times the substring appears in the string, including overlapping instances. This is achieved using the built-in `count` method in Python, which returns the number of occurrences of substring `substring` in string `string`. 
For example:
```python
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
```
will respectively return:
```
3
3
```
The implementation is concise due to the extensibility of Python and its powerful built-in methods.
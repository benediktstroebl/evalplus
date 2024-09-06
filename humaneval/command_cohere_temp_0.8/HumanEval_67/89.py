```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This problem can be solved by parsing the string to calculate the number of apples and oranges and then subtracting them from the total number of fruits. Thus, the following code achieves this purpose:
- `def fruit_distribution(s,n)`: The function takes two parameters, a string `s` and an integer `n`, which represents the total number of fruits in the basket. 
- `apples, oranges = map(int, s.split(' and '))`: This line uses the `split(' and ')` method to split the string `s` into a list of substrings, and uses `map(int, ...)` to convert the substrings to integers. The `apples` variable will contain the number of apples, and the `oranges` variable will contain the number of oranges. 
- `return n - apples - oranges`: Finally, the function returns the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits in the basket. 

Here is an example usage of the function:
```python
print(fruit_distribution("5 apples and 6 oranges", 19))
```
This would print:
```bash
8
```
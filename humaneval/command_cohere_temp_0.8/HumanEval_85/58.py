```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even elements at odd indices from the input list and then uses the `sum()` function to add these numbers. The function gracefully handles cases like empty lists, or lists with only odd or only even numbers without any exceptions. 
The function passes the given test case: `add([4, 2, 6, 7]) ==> 2`. 
Any list of integers provided as an argument will return the sum of its even elements that are located at odd indices. 
If you would like to test this script with more examples, you can add them in the comments, and the code will be modified to include the additional test cases. 
Let me know if you'd like to provide any specific test cases or if you have any other questions!
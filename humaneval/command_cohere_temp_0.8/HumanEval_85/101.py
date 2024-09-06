```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as an input. It aims to calculate the sum of even integers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the index of the element is odd and the element is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, which represents the desired sum of even integers at odd indices. 

Here is an example of how to use this function:
```python
my_list = [4, 2, 6, 7]
result = add(my_list)
print(result)
```
This will output: 
```
2
```
Which demonstrates that the function works as intended, as 2 is the sum of the even elements at odd indices in the list ([2, 6]).
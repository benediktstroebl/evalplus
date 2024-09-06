```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the current element is even and its index is odd (i.e., divisible by 1 but not by 2), it adds it to the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, which represents the total of even elements at odd indices in the original list. 

Here is an example of how to use this function:
```python
my_list = [4, 2, 6, 7]
result = add(my_list)
print(result)
```
For the provided example list my_list, the output will be 2, as explained in the problem statement.
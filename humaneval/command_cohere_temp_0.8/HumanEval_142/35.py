```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This function traverses the list using the enumerate function to access both the index and value of each entry. It applies the corresponding operation for squaring or cubing based on the index criteria and accumulates the sum of transformed and original numbers using the result variable. 
The syntax `enumerate(lst)` returns an enumerate object, which is a sequence of tuples, where each tuple contains a pair of values – the index of the element in the list and the value of the element itself. The for loop iterates over these tuples, i is the index and num is the value of the list element. Thus, the condition i % 3 == 0 checks if the index is a multiple of 3 and so on. 

This solution enables the proper manipulation of list entries while calculating the sum, aligning with the problem's requirement of altering only specific index elements. 

The sum_squares function gives the following output:
```
6
0
-126
```
corresponding to the examples provided in the question.
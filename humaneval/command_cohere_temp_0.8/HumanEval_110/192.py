```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        return "YES"
    else:
        li = 0
        for x in lst2:
            if type(x) == int and x % 2 == 0:
                li += 1
        if li == len(lst1):
            return "YES"
        else: 
            return "NO"
```
This code defines a function exchange that takes two lists, lst1 and lst2, and determines whether it is possible to exchange elements between them to make lst1 contain only even numbers. The function checks if there is at least one even number in lst1, and if so, returns "YES" since we can exchange all even numbers from lst1 with lst2. If there are no even numbers in lst1, the function checks if there is at least one even number in lst2, and if so, it counts how many even numbers are in lst2. If the count of even numbers in lst2 is the same as the length of lst1, it means we can make a successful exchange, and the function returns "YES". Otherwise, it returns "NO". The overall time complexity of this code is O(nm), where n is the length of lst1 and m is the length of lst2, and the space complexity is O(1) since it only uses constant space to store variables. 
```python
# Training data
lst1_1 = [1, 2, 3, 4]
lst2_1 = [1, 2, 3, 4]
assertEqual(exchange(lst1_1, lst2_1), "YES")

lst1_2 = [1, 2, 3, 4]
lst2_2 = [1, 5, 3, 4]
assertEqual(exchange(lst1_2, lst2_2), "NO")

lst1_3 = [2, 4, 6, 8]
lst2_3 = [1, 2, 3, 4]
assertEqual(exchange(lst1_3, lst2_3), "YES")

lst1_4 = [1, 2, 3, 5]
lst2_4 = [1, 2, 3, 4]
assertEqual(exchange(lst1_4, lst2_4), "NO")

# Example test
lst1 = [2, 4, 6]
lst2 = [8, 7, 9, 10]
assertEqual(exchange(lst1, lst2), "NO")
```
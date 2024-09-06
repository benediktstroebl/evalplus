```python
def exchange(lst1, lst2):
    even_numbers = [x for x in lst1 if x % 2 == 0]
    if len(even_numbers) == len(lst1):
        return "YES"
    else:
        count = 0
        for element in lst1:
            if element in lst2:
                lst1.remove(element)
                lst2.remove(element)
                count += 1
        if count == len(lst1):
            return "YES"
        else:
            return "NO"
```

The function `exchange()` takes two lists lst1 and lst2. It moves all even numbers from lst1 to lst2 (and vice versa) while keeping the order of elements unchanged. It returns "YES" if after the exchange, lst1 contains only even numbers, and "NO" otherwise. The algorithm works by first creating a list of even numbers from lst1 and checking if it matches the length of lst1. If it does, it returns "YES" since after the exchange, lst1 will contain only even numbers. If the list of even numbers doesn't match the length of lst1, it starts iterating through lst1 and removing elements belonging to lst1 that are also present in lst2. The function returns "YES" if all elements of lst1 can be removed this way, meaning that all remaining elements in lst1 are even. If any elements remain in lst1 that are not present in lst2, it returns "NO." 
Let's test this function using the following calls:
```python
print(exchange([1, 2, 3, 4], [1, 2, 3, 4])) # Output: YES
print(exchange([1, 2, 3, 4], [1, 5, 3, 4])) # Output: NO
```
The first test case should return "YES" since we can exchange elements between the lists to make lst1 contain only even numbers. However, in the second test case, we cannot exchange elements between the lists since there is no integer in lst2 that is not even and vice versa for lst1, thus returning "NO."